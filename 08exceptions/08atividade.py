'''
Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

try para a conversão,

else para verificar se é par ou ímpar,
finally para exibir "Fim do programa".
'''

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: você não digitou um número inteiro.")
else:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
finally:
    print("Fim do programa.")
