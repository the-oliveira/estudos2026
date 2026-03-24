#Programa que faça o computador sortear um numero entre 0 e 5
#Usuario vai tentar adivinhar o número
#Retorno será informando o usuário que ele venceu ou perdeu.
from random import randint
from time import sleep

print(f'Vamos ver se você acerta o número secreto!')
numero_magico = randint(0,5)
palpite_usuario = int(input(f'Chute o número secreto (0 a 5): '))

print('Hmm.... Deixe me pensar')
sleep(2)

if palpite_usuario == numero_magico:
    print(f'Você acertou! Era o {numero_magico}!')
else:
    print(f'Errouuu! o número era o {numero_magico}')