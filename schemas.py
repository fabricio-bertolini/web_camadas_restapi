from pydantic import BaseModel

class Eletronico(BaseModel):
    descricao: str
    tipo: str
    quantidade: int
    preco: int

