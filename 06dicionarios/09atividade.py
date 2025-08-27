'''
Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
'''

# Função para mesclar dois dicionários
def mesclar_dicionarios(d1, d2):
    novo_d = d1.copy()  
    # Cria uma cópia do primeiro dicionário
    novo_d.update(d2)   
    # Atualiza com o segundo dicionário, sobrescrevendo chaves iguais
    return novo_d

# Exemplos de dicionários
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4}

# Usando a função
resultado = mesclar_dicionarios(dict1, dict2)
print(resultado)
