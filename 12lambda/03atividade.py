'''
Soma dos números (reduce + lambda)

Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
'''

from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)