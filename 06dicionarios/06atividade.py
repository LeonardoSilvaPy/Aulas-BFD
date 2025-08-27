'''
Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
'''

# Lista de palavras
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# Função para contar palavras
def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

# Usando a função
resultado = contar_palavras(palavras)
print(resultado)
