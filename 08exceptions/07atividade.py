'''
Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

ValueError se o usuário digitar algo inválido

ZeroDivisionError se tentar dividir por zero
'''

try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    resultado = a / b
except ValueError:
    print("Erro: você deve digitar números válidos.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
else:
    print(f"O resultado da divisão é {resultado}")
