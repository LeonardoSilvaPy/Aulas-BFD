'''
Crie uma classe chamada Pessoa que tenha os atributos nome e idade.
Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Paula", 25)
pessoa2 = Pessoa("Ana", 30)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
