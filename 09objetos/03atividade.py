'''
Crie uma classe Carro com os atributos marca, modelo e ano.
Use o método __init__ para inicializar esses valores.
Crie três objetos e mostre suas informações.
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Fiesta", 2018)

print(carro1.marca, carro1.modelo, carro1.ano)
print(carro2.marca, carro2.modelo, carro2.ano)
print(carro3.marca, carro3.modelo, carro3.ano)
