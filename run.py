from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Incluir as rotas do chatbot
app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo ao Chatbot do Portfolio!"}
