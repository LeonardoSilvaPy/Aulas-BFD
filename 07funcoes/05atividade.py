'''
Crie uma função chamada operacoes que receba dois números e retorne a soma,
a subtração e a multiplicação deles.
'''

def operacoes(a, b):
    return a + b, a - b, a * b

soma, subtracao, multiplicacao = operacoes(10, 5)
print(soma, subtracao, multiplicacao)
