'''Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.'''

dia = int(input("Dias alugado: "))
km = int(input("Qulômetros percorrido: "))

preco_final = (dia * 60) + (km * 0.15)

print(f"O preço total é de R$ {preco_final:5.2f}")