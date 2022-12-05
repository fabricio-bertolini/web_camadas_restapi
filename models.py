from sqlalchemy import Column, Integer, String
from db import Base

class Eletronico(Base):
    __tablename__ = 'eletronicos'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(256))
    tipo = Column(String(256))
    quantidade = Column(Integer)
    preco = Column(Integer)
