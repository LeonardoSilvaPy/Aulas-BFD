'''
Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)
'''

import numpy as np

# Cria um tabuleiro 8x8 vazio usando list comprehension
tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

# Peças principais (torre, cavalo, bispo, rainha, rei, bispo, cavalo, torre)
linha_principal = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']

# Adicionando peças pretas (linha 0 e 1)
tabuleiro[0] = linha_principal
tabuleiro[1] = ['pea'] * 8

# Adicionando peças brancas (linha 6 e 7)
tabuleiro[6] = ['pea'] * 8
tabuleiro[7] = linha_principal

# Transformando em array para melhor visualização
tabuleiro_np = np.array(tabuleiro)

# Imprimindo o tabuleiro
for linha in tabuleiro_np:
    print(linha)
