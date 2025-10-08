'''
Interface em herança múltipla

Crie uma interface Imprimivel com o método imprimir().
Crie outra interface Exportavel com o método exportar().
Implemente uma classe Relatorio que herde de ambas e implemente os métodos.
'''

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Relatório impresso."

    def exportar(self):
        return "Relatório exportado."

relatorio = Relatorio()
print(relatorio.imprimir())
print(relatorio.exportar())
