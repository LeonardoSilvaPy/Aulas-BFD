'''
Filtrar pares (filter + lambda)

Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)
