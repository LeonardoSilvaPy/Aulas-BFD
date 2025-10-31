'''
Faça a query para pegar toda a tabela alunos e imprima na tela.
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
    for tabela in tabelas:
        print(f"- {tabela[0]}")

    print("\nConteúdo da tabela 'Aluno':\n")
    cur.execute("SELECT * FROM Aluno;")
    alunos = cur.fetchall()

    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(aluno)

con.close()
