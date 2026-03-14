#Ler um ângulo e mostrar o seno, cosseno e tangente do angulo
from math import tan as tangente, sin as seno, cos as cosseno, radians as rad

x = int(input('Digite um ângulo: '))
seno_x = seno(rad(x))
cosen_x = cosseno(rad(x))
tang_x = tangente(rad(x))

print(f'O seno, cosseno e tangente de {x}° são: ')
print(f'Seno: {seno_x:.2f}')
print(f'Cosseno: {cosen_x:.2f}')
print(f'Tangente: {tang_x:.2f}')