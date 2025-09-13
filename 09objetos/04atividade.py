'''
Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos
(por exemplo, mudar o ano). Imprima antes e depois da alteração.
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2020)

print("Antes da alteração:", carro1.marca, carro1.modelo, carro1.ano)

carro1.ano = 2023

print("Depois da alteração:", carro1.marca, carro1.modelo, carro1.ano)

