'''Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.'''

distancia = float(input("Qual a distância da viagem?: "))
vm = float(input("Velocidade média do veículo?: "))

tempo = distancia / vm

print(f"Você chegara em {tempo:.2f} horas")