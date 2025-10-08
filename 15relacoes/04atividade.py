'''
Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos,
enquanto Time agrega jogadores em uma lista.
'''

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        return [f"{j.nome} - {j.posicao}" for j in self.jogadores]

time = Time("Tigres FC")
j1 = Jogador("Carlos", "Atacante")
j2 = Jogador("Rafael", "Goleiro")

time.adicionar_jogador(j1)
time.adicionar_jogador(j2)

print(time.listar_jogadores())
