'''
Dado o dicionário:

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
Remova a chave "ano" do dicionário.
'''

# Dicionário inicial
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}

# Removendo a chave "ano"
carro.pop("ano")  # ou usar: del carro["ano"]

# Exibindo o dicionário atualizado
print(carro)
