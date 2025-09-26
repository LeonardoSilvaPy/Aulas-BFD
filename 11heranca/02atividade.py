'''
Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente.
Mostre como chamar o método herdado a partir de um objeto Cliente.
'''

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

cliente1 = Cliente("Leonardo", "leonardo@email.com")
cliente1.exibir_informacoes()
