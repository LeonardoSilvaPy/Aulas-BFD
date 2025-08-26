''''
Classificação de idade
    Ler a idade e dizer: 
        "Criança" (até 12 anos)
        "Adolescente" (13 a 17 anos)
        "Adulto" (18 a 64 anos) 
        "Idoso" (65 ou mais) 
'''
# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Classifica de acordo com a faixa etária
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")


