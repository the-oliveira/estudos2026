#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)


print(f'O número digitado foi {numero}')
print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz:.3}')