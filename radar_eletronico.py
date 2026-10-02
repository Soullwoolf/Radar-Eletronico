#Programa que le a velocidade de um carro.
#Se ele ultrapassar 80km/h. Mostra uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você execedeu a velocidade permitida da via e foi multado, a multa é de R${:.2f}'.format(multa))
else:
    print('Você esta em uma velocidade boa, tenha uma boa viagem!')

#Radar eletrônico!