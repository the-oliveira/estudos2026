#Programa mostra na tela todos os números pares entre 1 a 50

for n in range(1, 50+1):
    if n % 2 == 0:
        print(f'{n}', end=', ')
print('São os números pares!')