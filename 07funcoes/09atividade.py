'''
Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros.
A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:

 def soma(a, b): return a + b
 aplicar_operacao(3, 4, soma)
'''

def aplicar_operacao(a, b, func):
    return func(a, b)

def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicacao))

