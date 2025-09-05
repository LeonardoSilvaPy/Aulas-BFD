'''
Crie um programa que peça ao usuário um número inteiro.
Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
'''
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: você não digitou um número inteiro.")
else:
    print(f"Você digitou corretamente o número {numero}.")
