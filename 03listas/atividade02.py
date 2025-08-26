'''
Usando a lista criada na questão anterior, use o método insert ou append para
adicionar mais dois elementos a lista e use remove, pop ou del para remover um
elemento da lista.
'''

# Lista inicial com diferentes tipos de dados
minha_lista = [
    "Texto",          
    42,               
    3.14,             
    True,             
    [1, 2, 3],        
    {"nome": "Ana"},  
    (7, 8, 9)         
]

# Adicionando dois novos elementos
minha_lista.append("Novo elemento")  # Adiciona ao final
minha_lista.insert(2, 99)            # Insere o número 99 na posição 2

# Removendo um elemento da lista
minha_lista.remove(42)               # Remove o número 42

# Exibindo a lista final
print(minha_lista)
