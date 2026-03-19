#Programa que faça o computador sortear um numero entre 0 e 5
#Usuario vai tentar adivinhar o número
#Retorno será informando o usuário que ele venceu ou perdeu.
from random import randint

print(f'Vamos ver se você acerta o número secreto!')
numero_magico = randint(0,5)
palpite_usuario = int(input('Chute o número secreto (0 a 5): '))

if palpite_usuario == numero_magico:
    print('Você acertou!')
else:
    print('Errouuu!')