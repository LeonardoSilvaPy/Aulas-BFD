'''
Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
'''

# Lista atual
minha_lista = [
    "Musashi", "Duna", "Sussurro", "Amos Daragon", "Dom Quixote", "O Hobbit"
]

# Tentando remover "Silêncio dos inocentes"
livro_para_remover = "Silêncio dos inocentes"

if livro_para_remover in minha_lista:
    minha_lista.remove(livro_para_remover)
    print(f'O livro "{livro_para_remover}" foi removido.')
else:
    print("Livro não encontrado.")

# Exibindo a lista atualizada
print(minha_lista)
