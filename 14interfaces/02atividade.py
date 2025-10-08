'''
Interface múltipla

Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel
(com o método desligar()). Crie uma classe Computador que implemente ambas.
 Mostre seu uso.
'''

from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado."

    def desligar(self):
        return "Computador desligado."

pc = Computador()
print(pc.ligar())
print(pc.desligar())
