import sqlite3
from typing import Union
from models import CentroTreinamento, Atleta, Categoria, UpdateAtleta, UpdateCT

DATABASE_URI = "workout.db"
_connection: sqlite3.Connection

def get_sql_cursor() -> sqlite3.Cursor:
    global _connection
    _connection = sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return _connection.cursor()

def init_db(cursor: sqlite3.Cursor)-> None:
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Atleta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        cpf VARCHAR(11) UNIQUE,
        idade INTEGER NOT NULL,
        peso DECIMAL(5,2) NOT NULL,
        altura DECIMAL(5,2) NOT NULL,
        sexo VARCHAR(1),
        centro_treinamento_id INTEGER,
        categoria_id INTEGER,
        FOREIGN KEY(centro_treinamento_id)REFERENCES CentroTreinamento(id),
        FOREIGN KEY(categoria_id)REFERENCES Categoria(id)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS CentroTreinamento(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(20) UNIQUE NOT NULL,
        endereco VARCHAR(60) NOT NULL,
        proprietario VARCHAR(30) 
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(10) UNIQUE NOT NULL
        );
        '''
    )

def postCentro(centro:CentroTreinamento, cursor: sqlite3.Cursor)-> str:
    try:
        query = "INSERT INTO CentroTreinamento(nome,endereco,proprietario) VALUES (?,?,?);"
        values_tuple = (
            centro.nome,
            centro.endereco,
            centro.proprietario
        )
        cursor.execute(query,values_tuple)
        _connection.commit()
        situation = "Cadastro do centro de treinamento efetuado com sucesso!"
    except Exception as e:
        situation= f"Erro ao cadastrar centro de treinamento: {e}"
        _connection.rollback()
    return situation


def postCategoria(categoria: Categoria, cursor: sqlite3.Cursor)-> str:
    try:
        cursor.execute("INSERT INTO Categoria(nome) VALUES (?);", (categoria.nome,))
        _connection.commit()
        situation = "Cadastro de categoria efetuado com sucesso!"
    except Exception as e:
        situation= f"Erro no cadastro de categoria: {e}"
        _connection.rollback()
    return situation

def postAtleta(atleta: Atleta, cursor: sqlite3.Cursor)-> str:
    try:
        query = "INSERT INTO atleta(nome,cpf,idade,peso,altura,sexo,centro_treinamento_id,categoria_id) VALUES (?,?,?,?,?,?,?,?);"
        values_tuple = (
            atleta.nome,
            atleta.cpf,
            atleta.idade,
            atleta.peso,
            atleta.altura,
            atleta.sexo,
            atleta.centro_treinamento_id,
            atleta.categoria_id
        )
        cursor.execute(query,values_tuple)
        _connection.commit()
        situation = "Cadastro de atleta realizado com sucesso!"
    except Exception as e:
        situation = f"Erro no cadastro do atleta:{e}"
        _connection.rollback()
    return situation

def getCategorias(cursor:sqlite3.Cursor) -> Categoria:
    result = cursor.execute("SELECT * FROM categoria;")
    data = result.fetchall()
    return data

def getAtletas(cursor:sqlite3.Cursor) -> Atleta:
    query = '''
        SELECT at.nome,
        at.idade,
        at.peso,
        at.altura,
        ct.nome,
        cat.nome
        FROM Atleta at JOIN Categoria cat ON at.categoria_id = cat.id
        JOIN CentroTreinamento ct ON at.centro_treinamento_id = ct.id;   
    '''
    result = cursor.execute(query)
    data = result.fetchall()
    return data

def getAtletaID(id:int,cursor:sqlite3.Cursor) -> Union[Atleta,str]:
    query = '''
        SELECT at.nome,
        at.idade,
        at.peso,
        at.altura,
        ct.nome,
        cat.nome
        FROM Atleta at JOIN Categoria cat ON at.categoria_id = cat.id
        JOIN CentroTreinamento ct ON at.centro_treinamento_id = ct.id
        WHERE at.id = (?);
    '''
    result = cursor.execute(query,(id,))
    data = result.fetchone()
    if not data:
        return f"Não foi encontrado atleta com o id = {id}"
    else:
        return data 
    
def getCT(cursor: sqlite3.Cursor)-> CentroTreinamento:
    result = cursor.execute("SELECT * FROM CentroTreinamento")
    data=result.fetchall()
    return data

def delCT(id:int,cursor:sqlite3.Cursor)-> str:
    try:
        query = '''
            DELETE FROM CentroTreinamento WHERE id = (?);
        '''
        cursor.execute(query,(id,))
        _connection.commit()

        if cursor.rowcount > 0:
            situation = f"Centro de Treinamento id={id} deletado com sucesso!"
        else:
            situation = f"Nenhum Centro de Treinamento com id={id} foi encontrado!"
    except Exception as e:
        situation = f"Falha ao tentar deletar o Centro de treinamento de id={id}: {e}"
    return situation

def delCategoria(id:int,cursor:sqlite3.Cursor)-> str:
    try:
        query = '''
            DELETE FROM Categoria WHERE id=(?);
        '''
        cursor.execute(query,(id,))
        _connection.commit()

        if cursor.rowcount > 0:
            situation = f"Categoria id={id} deletado com sucesso!"
        else:
            situation = f"Nenhuma categoria com id={id} foi encontrado!"
    except Exception as e:
        situation = f"Falha ao tentar deletar a categoria de id={id}: {e}"
    return situation

def delAtleta(id:int,cursor:sqlite3.Cursor)-> str:
    try:
        query = '''
            DELETE FROM Atleta WHERE id=(?);
        '''
        cursor.execute(query,(id,))
        _connection.commit()

        if cursor.rowcount > 0:
            situation = f"Atleta id={id} deletado com sucesso!"
        else:
            situation = f"Nenhum atleta com id={id} foi encontrado!"
    except Exception as e:
        situation = f"Falha ao tentar deletar o atleta de id={id}: {e}"
    return situation

def AtualizarAtleta(id_atleta:int, atleta:UpdateAtleta, cursor:sqlite3.Cursor):
    try:
        query = '''
            UPDATE Atleta
            SET idade = ?,
            peso = ?,
            altura = ?,
            sexo = ?,
            centro_treinamento_id = ?,
            categoria_id = ?
            WHERE id = ?;
        '''
        values_tuple = (
            atleta.idade,
            atleta.peso,
            atleta.altura,
            atleta.sexo,
            atleta.centro_treinamento_id,
            atleta.categoria_id,
            id_atleta
        )
        cursor.execute(query,values_tuple)
        _connection.commit()
        situation = "Dados do atleta foram atualizados com sucesso!"
    except Exception as e:
        situation = f"Erro ao atualizar os dados do atleta: {e}"
        _connection.rollback()
    return situation

def AtualizarCT(id_ct:int, centro:UpdateCT, cursor:sqlite3.Cursor):
    try:
        query = '''
            UPDATE CentroTreinamento
            SET endereco = ?,
            proprietario = ?
            WHERE id = ?;
        '''
        values_tuple = (
            centro.endereco,
            centro.proprietario,
            id_ct
        )
        cursor.execute(query,values_tuple)
        _connection.commit()
        situation = "Dados do centro de treinamento foram atualizados com sucesso!"
    except Exception as e:
        situation = f"Erro ao atualizar os dados do centro de treinamento: {e}"
        _connection.rollback()
    return situation
