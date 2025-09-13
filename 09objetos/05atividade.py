'''
Crie uma classe ContaBancaria com os atributos titular e saldo.
Adicione um método depositar(valor) que aumenta o saldo e
um método sacar(valor) que diminui o saldo (se houver saldo suficiente).
Teste com depósitos e saques.
'''

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

conta1 = ContaBancaria("Leonardo", 500)

conta1.depositar(200)
conta1.sacar(100)
conta1.sacar(700)
