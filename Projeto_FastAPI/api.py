import sqlite3
import uvicorn
from fastapi import FastAPI
from actions import *
from models import Atleta, CentroTreinamento, Categoria, UpdateAtleta, UpdateCT
app = FastAPI(title = "WorkoutAPI")
cursor: sqlite3.Cursor

@app.on_event("startup")
def get_or_create_db():
    global cursor
    cursor = get_sql_cursor()
    init_db(cursor = cursor)


@app.post("/cadastrar_centro")
def post_centro_treinamento(centroTr: CentroTreinamento):
    resp = postCentro(centro = centroTr,cursor = cursor)
    return resp

@app.post("/cadastrar_categoria")
def post_categoria(categoria:Categoria):
    resp = postCategoria(categoria=categoria,cursor = cursor)
    return resp

@app.post("/cadastrar_atleta")
def post_atleta(atleta:Atleta):
    resp = postAtleta(atleta=atleta,cursor=cursor)
    return resp

@app.get("/consultar_categorias")
def get_categoria():
    resp = getCategorias(cursor=cursor)
    return resp

@app.get("/consultar_atletas")
def get_atletas():
    resp = getAtletas(cursor=cursor)
    return resp

@app.get("/consultar_atleta_por_id")
def get_atleta_id(id:int):
    resp = getAtletaID(id=id,cursor=cursor)
    return resp

@app.get("/consultar_centro_treinamento")
def get_ct():
    resp = getCT(cursor=cursor)
    return resp

@app.delete("/deletar_centro_treinamento")
def del_ct(id:int):
    resp = delCT(id,cursor=cursor)
    return resp

@app.delete("/deletar_categoria")
def del_categoria(id:int):
    resp = delCategoria(id,cursor=cursor)
    return resp

@app.delete("/deletar_atleta")
def del_atleta(id:int):
    resp = delAtleta(id, cursor=cursor)
    return resp

@app.put("/atualizar_atleta")
def update_atleta(id:int, atleta:UpdateAtleta):
    resp = AtualizarAtleta(id_atleta=id,atleta=atleta,cursor=cursor)
    return resp

@app.put("/atualizar_centro_treinamento")
def update_ct(id:int, centro:UpdateCT):
    resp = AtualizarCT(id_ct = id, centro=centro, cursor=cursor)
    return resp

if __name__ == "__main__":
    uvicorn.run("api:app", port = 8000,reload=True)