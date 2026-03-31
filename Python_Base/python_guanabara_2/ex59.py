#JOGO - Computador vai pensar em um número de 0 a 10
#Jogador vai tentar até acertar
#No final vai ter um contador com as tentativas até acertar
from time import sleep
from random import randint

num_computador = randint(0, 10) #Numero que o computador vai pensar
tentativas = 0 #Contador de tentativas


print('Vou pensar em um número de 0 a 10...')
sleep(1)
print('Vamos ver em quantas tentativas você acerta!')
sleep(1)
while True:
    palpite = int(input('Qual o seu palpite? '))
    tentativas += 1
    
    if palpite == num_computador:
        print(f'Você acertou! Pensei no número {palpite}!')
        break
    else:
        print('Errouu...')
        sleep(1)

sleep(1)
print(f'Você acertou em {tentativas}!')