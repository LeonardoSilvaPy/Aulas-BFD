'''
Dado o dicionário:

d = {"a": 1, "b": 2, "c": 3}
Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
'''

# Dicionário original
d = {"a": 1, "b": 2, "c": 3}

# Invertendo chaves e valores
d_invertido = {valor: chave for chave, valor in d.items()}

# Exibindo o dicionário invertido
print(d_invertido)
