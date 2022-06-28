from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from typing import Union

class Competicao(BaseModel):
    competicao: str
    atleta: str
    value: Union[float, list]
    unidade: str

app = FastAPI()

db = sqlite3.connect('database.db')
conn = db.cursor()

@app.get("/")
async def root():
    return {"message": "Exemplo de API com FastAPI"}


@app.post("/criar_competicao" )
async def criar_competicao(nome_competicao: str):
    dados = conn.execute( """SELECT COUNT (competicao)                            

                                  FROM competicoes
                                  WHERE competicao = ?""", (nome_competicao,) )
    contagem = dados.fetchall()[0][0]
    if contagem == 0:
        conn.execute( f"""INSERT 
                                  INTO competicoes (competicao, status) 
                                VALUES ('{nome_competicao}', '{0}')""" )
        db.commit()
        return {"message": "Competição criada com sucesso"}

    return {"message": "Essa competição já existe!"}
