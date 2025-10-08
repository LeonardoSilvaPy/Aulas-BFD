'''
Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro.
Se o Carro deixar de existir, o Motor também deixa.
Mostre isso criando e depois apagando o objeto.
'''

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor de {self.potencia} cavalos ligado."

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def ligar(self):
        return f"{self.modelo}: {self.motor.ligar()}"

carro = Carro("Sedan", 120)
print(carro.ligar())

del carro
print("O carro foi deletado e seu motor também deixou de existir.")
