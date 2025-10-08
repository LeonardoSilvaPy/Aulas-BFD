'''
Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.).
Cada Comodo deve ser criado dentro da Casa.
'''
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]

    def listar_comodos(self):
        return [c.nome for c in self.comodos]

casa = Casa()
print(casa.listar_comodos())
