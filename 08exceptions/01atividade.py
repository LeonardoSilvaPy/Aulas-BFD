'''
Escreva um programa que peça ao usuário para digitar um número.
Trate o erro caso ele digite algo que não seja um número inteiro.
'''

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou {numero}")
except ValueError:
    print("Erro: isso não é um número inteiro.")
