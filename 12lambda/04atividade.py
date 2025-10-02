'''
Ordenação por comprimento da palavra (sorted + lambda)

Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
'''

palavras = ["uva", "banana", "maçã", "laranja"]
palavras_ordenadas = sorted(palavras, key=lambda palavra: len(palavra))
print(palavras_ordenadas)