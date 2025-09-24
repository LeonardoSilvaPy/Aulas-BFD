''''
Crie uma classe, Pessoa, que tenha os atributos:
nome, data de nascimento, cpf, identidade.
Deixe os atributos cpf e identidade como privado
e monte os métodos setters e getters para acessar
e editar os valores
'''


class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = None
        self.__identidade = None
        self.set_cpf(cpf)
        self.set_identidade(identidade)

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, valor):
        if isinstance(valor, str) and len(valor) == 11 and valor.isdigit():
            self.__cpf = valor
        else:
            print("CPF inválido")

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, valor):
        if isinstance(valor, str) and valor.isdigit():
            self.__identidade = valor
        else:
            print("Identidade inválida")


p1 = Pessoa("Leonardo", "24/09/2000", "12345678901", "456789")
print(p1.get_cpf())
print(p1.get_identidade())
p1.set_cpf("98765432100")
print(p1.get_cpf())
