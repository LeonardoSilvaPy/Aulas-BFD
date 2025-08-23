'''
Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os
elementos da lista por 5. O resultado deve ser uma nova lista com os elementos
multiplicados.
'''
# Criando uma lista apenas com números
numeros = [2, 4.5, 7, 10, 3.2]

# Multiplicando cada elemento por 5 e criando uma nova lista
multiplicados = [num * 5 for num in numeros]

# Exibindo o resultado
print("Lista original:", numeros)
print("Lista multiplicada:", multiplicados)
