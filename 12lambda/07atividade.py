'''
Ordenar por último caractere (sorted + lambda)

Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
'''

palavras = ["banana", "uva", "maçã", "laranja"]
palavras_ordenadas = sorted(palavras, key=lambda x: x[-1])
print(palavras_ordenadas)