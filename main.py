from fastapi import FastAPI, status, HTTPException
from db import Base, engine
from sqlalchemy.orm import Session
import models, schemas

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return "Desenvolvimento WEB Camadas: Fabrício Valladares Bertolini, Guilherme Ferraz."

@app.post("/eletronicos", status_code=status.HTTP_201_CREATED)
def create_eletronico(eletronico: schemas.Eletronico):
    session = Session(bind=engine, expire_on_commit=False)
    eletronicomod = models.Eletronico(  descricao = eletronico.descricao, 
                                        tipo = eletronico.tipo, 
                                        quantidade = eletronico.quantidade, 
                                        preco = eletronico.preco)
    session.add(eletronicomod)
    session.commit()
    id = eletronicomod.id
    
    session.close()

    return f"Created Eletronico with id: {id}."

@app.get("/eletronicos/{id}")
def read_eletronico(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    eletronico = session.query(models.Eletronico).get(id)
    
    session.close()

    if not eletronico:
        raise HTTPException(status_code=404, detail=f"Eletronico item with id: {id} was not found.")

    return eletronico

@app.put("/eletronicos/{id}")
def update_eletronico(  id: int, 
                        descricao: str, 
                        tipo: str, 
                        quantidade: int, 
                        preco: int):
    session = Session(bind=engine, expire_on_commit=False)
    eletronico = session.query(models.Eletronico).get(id)

    if eletronico:
        eletronico.descricao = descricao
        eletronico.tipo = tipo
        eletronico.quantidade = quantidade
        eletronico.preco = preco
        session.commit()
    session.close()

    if not eletronico:
        raise HTTPException(status_code=404, detail=f"Eletronico with id: {id} was not found.")

    return eletronico

@app.delete("/eletronicos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_eletronico(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    eletronico = session.query(models.Eletronico).get(id)
    
    if eletronico:
        session.delete(eletronico)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Eletronico with id: {id} was not found.")

    return None

@app.get("/eletronicos")
def read_eletronico_list():
    session = Session(bind=engine, expire_on_commit=False)
    eletronico_list = session.query(models.Eletronico).all()

    session.close()

    return eletronico_list
