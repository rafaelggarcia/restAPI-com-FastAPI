from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from typing import Union

app = FastAPI()

db = sqlite3.connect('database.db')
conn = db.cursor()

@app.get("/")
async def root():
    return {"message": "Exemplo de API com FastAPI"}
