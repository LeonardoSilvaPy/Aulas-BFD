'''
 Somatória com while
    Ler números até o usuário digitar 0.
    Mostrar a soma dos números digitados. 
'''
# Acumulador para a soma
soma = 0  

while True:
    numero = float(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
# Adiciona o número à soma
    soma += numero  

print(f"A soma dos números digitados é: {soma}")


