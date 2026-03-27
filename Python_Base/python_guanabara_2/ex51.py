#Programa que lê 6 numeros inteiros e mostra a soma de todos os pares
sum_par = 0
c = 0

for n in range(1, 6+1):
    num = int(input('Digite um número: '))
    if num % 2 == 0 :
        sum_par += num
        c += 1

print(f'Você informou {c} números PARES e a soma total foi {sum_par}')