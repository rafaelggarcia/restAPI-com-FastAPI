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


@app.post("/inserir_dados")
async def inserir_dados(competicao: Competicao):
    if isinstance(competicao.value, float):
        competicao.value = competicao.value
    else:
        competicao.value = max(competicao.value)
    nome_competicao = competicao.competicao
    dados = conn.execute("""SELECT status from competicoes WHERE  competicao = ?""", (nome_competicao,) )
    print(dados)
    dados = dados.fetchall()
    print(dados)
    if len(dados) == 0:
        return {"message": "Essa competição ainda não foi aberta! Caso queira abrir uma nova competição utilize a rota /criar_competicao"}
    if dados[0][0] == 1:
        return {"message": "Essa competição já foi fechada!"}
    conn.execute(f"""INSERT
                     INTO resultados_competicoes (competicao, atleta, value, unidade)
                    VALUES ('{competicao.competicao}','{competicao.atleta}', {competicao.value}, '{competicao.unidade}')""")
    db.commit()
    return {"message": "Dados inseridos com sucesso"}
