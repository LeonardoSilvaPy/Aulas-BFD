'''
Forçando contrato

Crie uma interface Repositorio com os métodos salvar(objeto)
e buscar(id). Depois, crie uma classe RepositorioMemoria que
não implemente um dos métodos. O que acontece quando você tenta
instanciá-la? Corrija o código.
'''

from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"Objeto {objeto} salvo na memória."

try:
    repo = RepositorioMemoria()
except TypeError as e:
    print("Erro:", e)

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"Objeto {objeto} salvo na memória."

    def buscar(self, id):
        return f"Objeto com ID {id} encontrado."

repo = RepositorioMemoria()
print(repo.salvar("dados"))
print(repo.buscar(1))
