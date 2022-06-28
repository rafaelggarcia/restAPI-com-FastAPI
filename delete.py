import sqlite3

db = sqlite3.connect('database.db')

conn = db.cursor()

# apagar os dados da base

conn.execute("""DELETE FROM resultados_competicoes""")

conn.execute("""DELETE FROM competicoes""")


db.commit()
