'''
Faça uma cópia da lista da questão anterior. Use a função id para verificar se
realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista
e não uma nova)
'''
# Lista original
minha_lista = [
    "Texto",          
    99,               
    3.14,             
    True,             
    [1, 2, 3],        
    {"nome": "Ana"},  
    (7, 8, 9),
    "Novo elemento"
]

# Fazendo uma cópia da lista
copia_lista = minha_lista.copy()  
# Verificando os IDs
print("ID da lista original:", id(minha_lista))
print("ID da cópia:", id(copia_lista))

# Verificando se são diferentes listas
if id(minha_lista) != id(copia_lista):
    print("São listas diferentes!")
else:
    print("São a mesma lista!")
