'''
Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
'''

import sqlite3

con = sqlite3.connect("escola_v2.db")
cur = con.cursor()

cur.execute("""
    SELECT *
    FROM Aluno
    LEFT JOIN Turma
    ON Aluno.id_turma = Turma.id_turma
    WHERE Aluno.id_turma = 2;
""")

dados_turma2 = cur.fetchall()

if not dados_turma2:
    print("Nenhum aluno encontrado na turma 2.")
else:
    print("Alunos da turma 2:\n")
    for linha in dados_turma2:
        print(linha)

con.close()
