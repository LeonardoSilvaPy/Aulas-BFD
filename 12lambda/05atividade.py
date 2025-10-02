'''
Primeira letra maiúscula (map + lambda)

Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].
'''

nomes = ["ana", "pedro", "maria"]
nomes_formatados = list(map(lambda x: x.capitalize(), nomes))
print(nomes_formatados)
