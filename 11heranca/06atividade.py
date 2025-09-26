'''
Crie uma classe Autenticacao com um método login().
Crie outra classe Permissao com um método verificar_permissao().
Em seguida, crie uma classe Administrador que herda de ambas.
Como usar os métodos herdados?
'''

class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login realizado com sucesso"
        return "Falha na autenticação"

class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            return "Permissão concedida"
        return "Permissão negada"

class Administrador(Autenticacao, Permissao):
    def __init__(self, usuario, senha, nivel):
        self.usuario = usuario
        self.senha = senha
        self.nivel = nivel

admin1 = Administrador("admin", "1234", "admin")

print(admin1.login(admin1.usuario, admin1.senha))
print(admin1.verificar_permissao(admin1.nivel))
