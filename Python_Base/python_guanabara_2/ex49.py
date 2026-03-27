#Calcule a soma de todos os números impares que são multiplos de 3 dentro do intervalo de 1 a 500
s = 0
cont = 0

for n in range(0, 500+1):
    if n % 2 != 0 and n % 3 == 0:
        s += n
        cont += 1

print(f'Soma dos {cont} valores = {s}')