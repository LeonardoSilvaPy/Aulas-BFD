'''
Exercício 10: Desafio do troco
    O programa deve receber o valor de uma compra e o valor pago pelo cliente. Calcular e mostrar o
    troco.
'''

valor_da_compra  = int((input("Informe o valor da compra : ")))
valor_pago       = int((input("Informe o valor pago      : ")))
print("O valor do troco é : ", valor_pago - valor_da_compra)