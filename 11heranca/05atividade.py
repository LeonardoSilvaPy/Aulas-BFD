'''
Crie uma classe Funcionario que herda de Usuario e, em seguida,
crie uma classe Gerente que herda de Funcionario. Mostre como
instanciar um gerente e acessar seus atributos.
'''

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, setor):
        super().__init__(nome, email, cargo)
        self.setor = setor

gerente1 = Gerente("Marcos", "marcos@email.com", "Gerente", "Vendas")

print(gerente1.nome)
print(gerente1.email)
print(gerente1.cargo)
print(gerente1.setor)
