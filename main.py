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


@app.get("/ranking/{competicao}")
async def ranking(competicao: str):
    if competicao == "corrida100m":
        dados = conn.execute( """SELECT atleta,                                
                                           RANK() OVER (ORDER BY value ASC) AS posicao_ranking, 
                                           value
                                      FROM resultados_competicoes
                                      WHERE competicao = ?""", (competicao,) )
    elif competicao == "dardo":
        dados = conn.execute("""SELECT atleta,                                
                                           RANK() OVER (ORDER BY value DESC) AS posicao_ranking,
                                           value
                                      FROM resultados_competicoes
                                      WHERE competicao = ?""", (competicao,) )
    else:
        dados = conn.execute( """SELECT atleta,                                
                                                   RANK() OVER (ORDER BY value DESC) AS posicao_ranking,
                                                   value
                                              FROM resultados_competicoes
                                              WHERE competicao = ?""", (competicao,))
    dados = dados.fetchall()
    dict_dados = {}
    for dado in dados:
        dict_dados[dado[0]] = {"ranking": dado[1], "value": dado[2]}
    return dict_dados


@app.post("/fechar_competicao")
async def fechar_competicao(nome_competicao: str):
    dados = conn.execute( """SELECT COUNT (competicao)                            

                                      FROM competicoes
                                      WHERE competicao = ?""", (nome_competicao,) )
    contagem = dados.fetchall()[0][0]
    if contagem == 1:
        conn.execute(""" UPDATE competicoes
        SET 
        status = 1
        WHERE competicao = ?""", (nome_competicao,) )
        db.commit()
        return {"message": "Competição finalizada com sucesso!"}
    return {"message": "Essa competição ainda não foi aberta! Caso queira abrir uma nova competição utilize a rota /criar_competicao"}