'''
Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao.
Se a classe Administrador herda das duas, qual versão de status() será chamada?
Use Administrador.__mro__ para mostrar a ordem.
'''

class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login realizado com sucesso"
        return "Falha na autenticação"

    def status(self):
        return "Status da Autenticação"

class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            return "Permissão concedida"
        return "Permissão negada"

    def status(self):
        return "Status da Permissão"

class Administrador(Autenticacao, Permissao):
    def __init__(self, usuario, senha, nivel):
        self.usuario = usuario
        self.senha = senha
        self.nivel = nivel

admin1 = Administrador("admin", "1234", "admin")

print(admin1.status())
print(Administrador.__mro__)
