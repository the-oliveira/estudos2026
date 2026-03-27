#Programa recebe um número inteiro e converta para uma das opções:
#Binário, octal ou hexadecimal (criar um menu para ele escohler uma opção e realizar a conversão)
from time import sleep

num = int(input('Digite um número: '))

print('Menu de conversão:')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

escolha = int(input('Deseja converter para qual opção? '))

if escolha == 1:
    print(f'{num} em Binário = {bin(num).replace('0b', '')}')
elif escolha == 2:
    print(f'{num} em Octal = {oct(num).replace('0o', '')}')
elif escolha == 3:
    print(f'{num} em Hexadecimal = {hex(num).replace('0x', '')}')
else:
    print(f'{escolha} não é uma opção válida, tente novamente...')