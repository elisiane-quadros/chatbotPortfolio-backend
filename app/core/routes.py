import json
import uuid
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .config import settings
from groq import Groq
from app.core.db import SessionLocal
from app.models.session import ChatSession
from app.services.chatbot_service import get_predefined_response

client = Groq(api_key=settings.GROQ_API_KEY)

router = APIRouter()

class UserMessage(BaseModel):
    message: str
    name: str = None

# Dependência para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat")
async def chat_with_user(user_message: UserMessage, db: Session = Depends(get_db)):
    try:
        predefined_reply = get_predefined_response(user_message.message)
        if predefined_reply:
            full_reply = json.dumps(predefined_reply)
        else:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_message.message}],
                model="llama3-8b-8192",
            )
            chatbot_reply = response.choices[0].message.content
            full_reply = json.dumps({"response": chatbot_reply, "options": []})  
        chat_session = ChatSession(
            session_id=str(uuid.uuid4()),  
            user_message=user_message.message,
            bot_response=full_reply
        )
        db.add(chat_session)
        db.commit()
        db.refresh(chat_session)

        # Retorna a resposta como JSON para o front-end
        return {"reply": json.loads(full_reply)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
