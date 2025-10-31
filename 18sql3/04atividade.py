'''
Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
'''

import sqlite3

con = sqlite3.connect("escola_v2.db")
cur = con.cursor()

cur.execute("""
    SELECT *
    FROM Aluno
    LEFT JOIN Turma
    ON Aluno.id_turma = Turma.id_turma;
""")

dados = cur.fetchall()

if not dados:
    print("Nenhum dado encontrado.")
else:
    print("Dados combinados entre Aluno e Turma:\n")
    for linha in dados:
        print(linha)

con.close()
