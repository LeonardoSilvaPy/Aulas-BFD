'''
Crie uma função chamada calculadora que tenha dentro dela outras funções
(somar, subtrair, multiplicar, dividir).
A função principal deve permitir escolher a operação e retornar o resultado.
'''

def calculadora(a, b, operacao):
    def somar(x, y):
        return x + y
    def subtrair(x, y):
        return x - y
    def multiplicar(x, y):
        return x * y
    def dividir(x, y):
        return x / y

    if operacao == "somar":
        return somar(a, b)
    elif operacao == "subtrair":
        return subtrair(a, b)
    elif operacao == "multiplicar":
        return multiplicar(a, b)
    elif operacao == "dividir":
        return dividir(a, b)

print(calculadora(10, 5, "somar"))
print(calculadora(10, 5, "subtrair"))
print(calculadora(10, 5, "multiplicar"))
print(calculadora(10, 5, "dividir"))
