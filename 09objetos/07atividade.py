'''
Crie uma classe Aluno com atributos nome e nota.
Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno).
Crie alguns objetos Aluno e adicione-os à turma.
'''

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")

aluno1 = Aluno("Leonardo", 9.0)
aluno2 = Aluno("Maria", 8.5)
aluno3 = Aluno("João", 7.0)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

turma.listar_alunos()
