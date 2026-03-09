#Aula de módulos
#Comando import para importar os módulos
#usar o from para puxar as funcionalidades que precisa, sem precisar importar o módulo inteiro

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é: {raiz:.2f}')
