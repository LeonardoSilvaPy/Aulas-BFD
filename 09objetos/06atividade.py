'''
Modifique a classe ContaBancaria para que o método sacar retorne 
True se a operação for bem-sucedida e False caso contrário. 
Teste o retorno e imprima mensagens adequadas.
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
            return True
        else:
            return False

conta1 = ContaBancaria("Leonardo", 500)

conta1.depositar(200)

if conta1.sacar(100):
    print("Saque realizado com sucesso.")
else:
    print("Falha no saque. Saldo insuficiente.")

if conta1.sacar(700):
    print("Saque realizado com sucesso.")
else:
    print("Falha no saque. Saldo insuficiente.")
