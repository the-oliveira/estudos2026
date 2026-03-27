#Programa lê um número inteiro e diz se é um número primo
divisiveis = []
num = int(input('Digite um número: '))

for n in range(1, num + 1):
    if num % n == 0:
        divisiveis.append(n)

if len(divisiveis) == 2:
    print(f'O número {num} é PRIMO')
else:
    print(f'O número {num} NÃO É PRIMO')