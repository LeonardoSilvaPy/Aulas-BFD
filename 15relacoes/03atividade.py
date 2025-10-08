'''
Crie uma classe Funcionario e Departamento que contém uma lista de
Funcionarios.Departamento deve agregar funcionários já criados.
'''

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        return [f.nome for f in self.funcionarios]

f1 = Funcionario("Ana")
f2 = Funcionario("João")
departamento = Departamento("Recursos Humanos")
departamento.adicionar_funcionario(f1)
departamento.adicionar_funcionario(f2)

print(departamento.listar_funcionarios())
