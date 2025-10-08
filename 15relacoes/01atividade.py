'''
Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor = Pessoa("Leonardo Silva")
livro = Livro("Programando em Python", autor)

print(f"O livro '{livro.titulo}' foi escrito por {livro.autor.nome}.")
