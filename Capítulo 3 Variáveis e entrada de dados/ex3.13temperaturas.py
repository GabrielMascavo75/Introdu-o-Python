'''Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: F=((9*C)/5)+32'''

celsius = float(input("Insira a temperatura em C°:"))

fahreinheint = ((9*celsius)/5)+32

print(f"A temperatura atual em F°{fahreinheint:.2f}")