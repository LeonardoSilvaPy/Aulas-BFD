'''
Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em
Cliente que inicialize também os atributos de Usuario usando super().
'''

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente"

cliente1 = Cliente("Leonardo", "leonardo@email.com", 1500)

print(cliente1.nome)
print(cliente1.email)
print(cliente1.saldo)
print(cliente1.saudacao())
