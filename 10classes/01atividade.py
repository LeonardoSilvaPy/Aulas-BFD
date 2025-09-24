'''
Na classe, ContaBancaria, converta saldo para uma atributo privado.
Crie um método setter e um getter para acessar e modificar essa atributo,
seguindo uma regra lógica (Ex: saldo não pode ser negativo)
'''

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = 0 
        self.set_saldo(saldo_inicial)

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo.")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saque inválido. Saldo insuficiente ou valor incorreto.")


conta = ContaBancaria("Leonardo", 100)

print("Saldo atual:", conta.get_saldo()) 
conta.depositar(50)
print("Saldo após depósito:", conta.get_saldo()) 
conta.sacar(200)  
conta.set_saldo(-500) 
