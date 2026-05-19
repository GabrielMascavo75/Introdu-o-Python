'''Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a portcentagem do aumento. Exiba o valor do aumento e do novo salário.'''

salario = float(input("Salário: R$"))
aumento_percentual = float(input("Aumento percentual: "))

aumento = (salario*aumento_percentual) / 100
novo_salario = salario + aumento

print(f"Você teve um aumento de R${aumento:.2f}, passara a receber R${novo_salario}")