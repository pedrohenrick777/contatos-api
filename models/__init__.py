from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .contatos import Contatos
from typing import List


DATABASE_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DATABASE_URL)


class ContatosRepo:
    def __init__(self):
        session_local = sessionmaker(bind=engine)
        self.db: Session = session_local()

    def find_all(self) -> List[Contatos]: 
        return self.db.query(Contatos).all()
    
    def save(self, contato: Contatos) -> Contatos:
        if contato.id:
            self.db.merge(contato)
        else:
            self.db.add(contato)

        self.db.commit()
        return contato
    
    def filter_by_id(self, id: int) -> Contatos:
        return self.db.query(Contatos).filter(Contatos.id == id).first()
    
    def exists_by_id(self, id: int) -> bool:
        return self.db.query(Contatos).filter(Contatos.id == id).first() is not None
    
    def delete_by_id(self, id: int):
        contato = self.db.query(Contatos).filter(Contatos.id == id).first()
        if contato is not None:
            self.db.delete(contato)
            self.db.commit( )