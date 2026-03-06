#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
numero = int(input('Digite um número: '))
raiz = numero ** (1/2)

print(f'O número digitado foi {numero}')
print(f'O dobro de {numero} é {numero * 2}')
print(f'O triplo de {numero} é {numero * 3}')
print(f'A raiz quadrada de {numero} é {raiz:.3}')