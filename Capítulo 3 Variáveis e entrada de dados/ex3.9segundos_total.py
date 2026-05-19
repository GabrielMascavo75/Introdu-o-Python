'''Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.'''
dias = int(input("Insira todos os dias: "))
horas = int(input("Insira todas as horas: "))
minutos = int(input("Insira todos os minutos: "))
segundos = int(input("Insira todos os segundos: "))

t_dias = dias * 86.400
t_horas = horas * 3600
t_minutos = minutos * 60
t_segundos = t_dias + t_horas + t_minutos + segundos

print(f"O total de segundos somados são {t_segundos} segundos")