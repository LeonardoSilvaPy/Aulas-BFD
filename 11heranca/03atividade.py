'''
Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".
Mostre como funciona a chamada.
'''

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def saudacao(self):
        return "Olá, cliente"

usuario1 = Usuario("João", "joao@email.com")
cliente1 = Cliente("Leonardo", "leonardo@email.com")

print(usuario1.saudacao())
print(cliente1.saudacao())
