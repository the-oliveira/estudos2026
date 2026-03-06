#Programa que leia um valor inteiro e faça a tabuada dele:
numero = int(input('Digite um valor inteiro: '))
n = 0

while n <= 10:
    print(f'{numero} x {n} = {numero * n}')
    n += 1