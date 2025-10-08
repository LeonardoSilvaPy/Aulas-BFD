'''
Criando uma interface

Crie uma interface chamada Pagamento com um método abstrato processar(valor).
 Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
 Mostre como chamar processar() para cada uma.
'''
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Pagamento de R${valor:.2f} processado com cartão de crédito."

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Pagamento de R${valor:.2f} processado via boleto bancário."

cartao = CartaoCredito()
boleto = Boleto()

print(cartao.processar(150.0))
print(boleto.processar(200.0))
