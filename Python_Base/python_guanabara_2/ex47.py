#Contagem regressiva de final de ano, de 10 até 0 esperando 1 segundo
from time import sleep

print('='*45)
print('Ultimos 10 segundos do ano!! Hora da contagem')
print('='*45)

for n in range(10, 0, -1):
    print(f'{n:^45}')
    sleep(1)

print(f'{' Feliz ano novo!!! ':-^45}')