'''
Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
'''

import sqlite3

con = sqlite3.connect("escola_v2.db")
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cur.fetchall()

if not tabelas:
    print("Nenhuma tabela encontrada no banco 'escola_v2.db'.")
else:
    print("Tabelas encontradas no banco 'escola_v2.db':\n")

con.close()
