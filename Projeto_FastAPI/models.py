from pydantic import BaseModel, create_model
from typing import Optional

class Atleta (BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int


class CentroTreinamento(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class Categoria(BaseModel):
    nome:str

class UpdateAtleta(BaseModel):
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int

class UpdateCT(BaseModel):
    endereco: str
    proprietario: str