'''
Crie uma função chamada media que receba uma quantidade variável de números
e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
'''

def media(*numeros):
    return sum(numeros) / len(numeros)

print(media(10, 20, 30))
print(media(5, 15, 25, 35, 45))
print(media(2, 4, 6, 8, 10, 12, 14))
