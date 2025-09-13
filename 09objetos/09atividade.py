'''
Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" 
e atributos de instância nome e idade. Mostre a diferença entre acessar especie 
pelo objeto e pela classe.
'''

class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

cachorro1 = Cachorro("Rex", 5)

print(cachorro1.nome, cachorro1.idade)
print(cachorro1.especie)
print(Cachorro.especie)
