''' Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a acada cigarro, quantos dias de vida um fumante perderá. Exiba o total em dias.'''

n_dia = int(input("Quantos cigarros fuma ao dia?: "))
n_anos = int(input("Fuma a quantos anos?: "))

total_cigarros = (n_anos * 365) * n_dia
perda_vida = total_cigarros * 10
morte = perda_vida / 1440
print(f"Você perdeu {morte:.0f} dias de vida")