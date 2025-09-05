'''
Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

"Olá, [nome]!"

          Caso o nome não seja informado, mostre "Olá, visitante!".
'''

def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

mensagem("Leonardo")
mensagem()
