#Programa que recebe 3 seguimentos de retas e vai responder se pode ou não formar um triangulo.
n1 = float(input('Digite o primeiro lado: '))
n2 = float(input('Digite o segundo lado: '))
n3 = float(input('Digite o terceiro lado: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triangulo.')