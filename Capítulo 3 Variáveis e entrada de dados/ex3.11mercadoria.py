'''Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.'''

valor = float(input("Preço do produto:R$ "))
percentual_desconto = float(input("Percentual do desconto:"))

desconto = (valor * percentual_desconto)/100
preco_novo = valor - desconto

print(f"Desconto de R${desconto:.2f}, valor a pagar de R${preco_novo:.2f}")