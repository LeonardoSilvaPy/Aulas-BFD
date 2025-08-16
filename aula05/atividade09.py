'''
Calculadora simples
Criar funções:
    somar(a, b)
    subtrair(a, b)
    multiplicar(a, b)
    dividir(a, b)
Permitir que o usuário escolha a operação. 
'''
# Definição das funções
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Menu para o usuário escolher a operação
print("=== Calculadora ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha a operação (1/2/3/4): ")

# Solicita os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executa a operação escolhida
if opcao == "1":
    resultado = somar(num1, num2)
elif opcao == "2":
    resultado = subtrair(num1, num2)
elif opcao == "3":
    resultado = multiplicar(num1, num2)
elif opcao == "4":
    resultado = dividir(num1, num2)
else:
    resultado = "Opção inválida"

# Exibe o resultado
print(f"Resultado: {resultado}")

