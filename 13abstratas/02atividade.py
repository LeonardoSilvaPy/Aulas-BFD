'''
Proibição de instanciamento

Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.
'''


'animal = Animal()'



'''
TypeError: Can't instantiate abstract class Animal with abstract method falar

Esse erro ocorre porque Animal é uma classe abstrata que possui um método abstrato (falar).
O Python proíbe a criação de instâncias de classes abstratas até que todos os métodos abstratos sejam implementados em uma subclasse concreta.
'''