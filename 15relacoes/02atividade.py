'''
Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
'''

class Onibus:
    def __init__(self, numero):
        self.numero = numero

    def embarcar(self, aluno):
        return f"{aluno.nome} embarcou no ônibus {self.numero}."

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        return onibus.embarcar(self)

onibus = Onibus(42)
aluno = Aluno("Lucas")

print(aluno.pegar_onibus(onibus))
