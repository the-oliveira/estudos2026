#Programa que recebe um número real(float) e mostra a porção inteira(antes da virgula)
from math import floor
num = float(input('Digite um valor real: '))

print(f'A parte inteira de {num} é {floor(num)}')