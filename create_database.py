import sqlite3

db = sqlite3.connect('database.db')

conn = db.cursor()

# create table
conn.execute("""CREATE TABLE IF NOT EXISTS resultados_competicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    competicao TEXT,
    atleta TEXT,
    value FLOAT,
    unidade TEXT)""")


conn.execute("""CREATE TABLE IF NOT EXISTS competicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    competicao TEXT,
    status INT)""")

db.commit()