from pydantic import BaseModel


class ContatoBase(BaseModel):
    nome: str
    telefone: str
    email: str

class ContatoRequest(ContatoBase):
    ...

class ContatoResponse(ContatoBase):
    id: int

    class Config:
        orm_mode = True