'''
Crie uma função chamada dados_pessoais que receba informações de uma pessoa
(nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha.
Exemplo de chamada:

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
'''

def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
