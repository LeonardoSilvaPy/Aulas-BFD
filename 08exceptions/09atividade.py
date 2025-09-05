'''
Crie uma função sacar(saldo, valor) que:

Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.

Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e
exiba uma mensagem apropriada ao usuário.
'''

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para saque.")
    return saldo - valor

saldo_atual = 100

try:
    novo_saldo = sacar(saldo_atual, 150)
    print(f"Saque realizado. Novo saldo: {novo_saldo}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
