''''
Aprovação escolar ○ Ler a nota de um aluno.
    Mostrar: 
    "Aprovado" se a nota for ≥ 7 
    "Recuperação" se estiver entre 5 e 6.9 
    "Reprovado" se for < 5. 
'''
# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica a situação do aluno
if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
