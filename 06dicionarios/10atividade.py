'''
Dado o dicionário:

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

'''
# Dicionário de pontuações
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# Ordenando os itens do dicionário pelo valor, do maior para o menor
ordenado = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)

# Exibindo os itens ordenados
for nome, pontuacao in ordenado:
    print(f"{nome}: {pontuacao}")
