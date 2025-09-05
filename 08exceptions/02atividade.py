'''
Peça ao usuário dois números e tente multiplicá-los.
Se o usuário digitar algo inválido, exiba uma mensagem de erro.
'''

try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(f"O resultado da multiplicação é {a * b}")
except ValueError:
    print("Erro: um dos valores digitados não é um número válido.")
