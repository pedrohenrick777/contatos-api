from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()

class Contatos(base):
    __tablename__ = 'contatos'

    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String)
    telefone: str = Column(String)
    email: str = Column(String)