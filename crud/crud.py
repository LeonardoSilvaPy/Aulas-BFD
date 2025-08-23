
usuarios = [] 

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    usuarios.append(nome)
    print("Usuário adicionado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        print("\nLista de usuários:")
        for i, nome in enumerate(usuarios):
            print(f"{i} - {nome}")
        print()

def atualizar_usuario():
    listar_usuarios()
    indice = int(input("Digite o índice do usuário que deseja atualizar: "))
    if 0 <= indice < len(usuarios):
        novo_nome = input("Digite o novo nome: ")
        usuarios[indice] = novo_nome
        print("Usuário atualizado com sucesso!\n")
    else:
        print("Índice inválido!\n")

def deletar_usuario():
    listar_usuarios()
    indice = int(input("Digite o índice do usuário que deseja excluir: "))
    if 0 <= indice < len(usuarios):
        usuarios.pop(indice)
        print("Usuário removido com sucesso!\n")
    else:
        print("Índice inválido!\n")

# Menu principal
while True:
    print("=== CRUD de Usuários ===")
    print("1 - Criar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        atualizar_usuario()
    elif opcao == "4":
        deletar_usuario()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")
