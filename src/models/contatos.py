from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()

class Contatos(base):
    __tablename__ = 'contatos'

    id: Column[int] = Column(Integer, primary_key=True)
    nome: Column[str] = Column(String)
    telefone: Column[str] = Column(String)
    email: Column[str] = Column(String)
