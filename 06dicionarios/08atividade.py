'''
Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
'''

# Dicionário com alunos e suas notas
notas_alunos = {
    "Lucas": [7, 8, 9],
    "Ana": [6, 9, 8],
    "Carlos": [10, 7, 9]
}

# Calculando e exibindo a média de cada aluno
for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média de {aluno} é: {media:.2f}")
