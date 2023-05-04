from fastapi import FastAPI, status, Response
from models.contatos import base, Contatos
from models import engine, ContatosRepo
from schemas.contato import ContatoRequest, ContatoResponse

base.metadata.create_all(bind=engine)

app = FastAPI()
contatos_repo = ContatosRepo()


@app.get('/list_contatos')
def list_contatos():
    contatos = contatos_repo.find_all()
    return [ContatoResponse.from_orm(contato) for contato in contatos]


@app.post('/create_contato', response_model=ContatoResponse, status_code=status.HTTP_201_CREATED)
def create_contato(request: ContatoRequest):
    contato = contatos_repo.save(Contatos(**request.dict()))
    return ContatoResponse.from_orm(contato)


@app.get('/contato/{id}')
def get_contato(id: int):
    contato = contatos_repo.filter_by_id(id)
    if not contato:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return ContatoResponse.from_orm(contato)


@app.delete('/contato/{id}')
def delete_contato(id: int):
    if not contatos_repo.exists_by_id(id):
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    contatos_repo.delete_by_id(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/contato/{id}')
def update_contato(id: int, request: ContatoRequest):
    if not contatos_repo.exists_by_id(id):
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        
    contato = contatos_repo.save(Contatos(id=id, **request.dict()))
    return ContatoResponse.from_orm(contato)