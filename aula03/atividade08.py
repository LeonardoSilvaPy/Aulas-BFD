'''
Exercício 8: Idade em dias
    Crie um programa que receba a idade de uma pessoa e calcule quantos dias ela já viveu
    (aproximadamente, desconsidere anos bissextos).
'''

idade = int((input("Informe sua idade: ")))
dias  = idade*365
bisexto = idade//4
print("Você viveu por ", dias+bisexto, " dias")