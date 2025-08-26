'''
1. Par ou ímpar
Peça para o aluno digitar um número. 
O programa deve dizer se ele é par ou ímpar. 
'''

# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Verifica se é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

