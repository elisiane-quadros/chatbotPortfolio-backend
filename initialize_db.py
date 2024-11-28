from app.core.db import Base, engine
from app.models.session import ChatSession

Base.metadata.create_all(bind=engine)

print("Banco de dados inicializado com sucesso!")

