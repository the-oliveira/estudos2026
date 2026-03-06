#Programa que leia um valor inteiro e faça a tabuada dele:
numero = int(input('Digite um valor inteiro: '))
n = 0

print('='*20)

while n <= 10:
    print(f'{numero} x {n:2} = {numero * n}')
    n += 1

print('='*20)