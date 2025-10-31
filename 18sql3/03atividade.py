'''
Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas.
No fim imprima na tela a lista desses alunos e suas médias.
'''

import sqlite3

con = sqlite3.connect("escola_v2.db")
cur = con.cursor()

cur.execute("""
    SELECT nome, (nota1 + nota2) / 2 AS media
    FROM Aluno
    ORDER BY media DESC
    LIMIT 10;
""")

top_alunos = cur.fetchall()

if not top_alunos:
    print("Nenhum aluno encontrado.")
else:
    print("Top 10 alunos com maiores médias:\n")
    for aluno in top_alunos:
        print(f"{aluno[0]} - Média: {aluno[1]:.2f}")

con.close()
