'''
 Tabuada ○ Pedir um número ao usuário e imprimir a tabuada desse número (de 1 a 10). 
'''
# Solicita um número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Imprime a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

