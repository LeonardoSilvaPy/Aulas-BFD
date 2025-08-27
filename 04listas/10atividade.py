'''
Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
'''

# Lista principal para armazenar as notas de todos os alunos
notas = []

# Coletando notas de 2 alunos
for i in range(2):
    aluno_notas = []  # Lista para armazenar as notas de cada aluno
    print(f"\nDigite as 3 notas do aluno {i + 1}:")
    
    for j in range(3):
        nota = float(input(f"Nota {j + 1}: "))
        aluno_notas.append(nota)
    
    notas.append(aluno_notas)

# Calculando e exibindo a média de cada aluno
for i, aluno in enumerate(notas, start=1):
    media = sum(aluno) / len(aluno)
    print(f"A média do aluno {i} é: {media:.2f}")
