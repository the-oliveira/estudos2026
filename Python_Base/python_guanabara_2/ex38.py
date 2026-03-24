#Programa recebe um número inteiro e converta para uma das opções:
#Binário, octal ou hexadecimal (criar um menu para ele escohler uma opção e realizar a conversão)
from time import sleep

num = int(input('Digite um número: '))

sleep(2)
print('Menu de conversão:')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
sleep(3)

escolha = int(input('Deseja converter para qual opção? '))

if escolha == 1:
    print(f'{num} em Binário = {bin(num)}')
elif escolha == 2:
    print(f'{num} em Octal = {oct(num)}')
else:
    print(f'{num} em Hexadecimal = {hex(num)}')
