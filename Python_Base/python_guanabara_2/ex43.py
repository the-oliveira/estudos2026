#Leia 3 seguimentos de reta e se ele puder formar o triangulo, deve informar o seguinte:
#Equilátero (todos lados iguais)
#Isósceles (dois lados iguais)
#Escaleno (Todos os lados diferentes)

l1 = float(input('Tamanho da primeira reta: '))
l2 = float(input('Tamanho da segunda reta: '))
l3 = float(input('Tamanho da terceira reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'As retas {l1}, {l2} e {l3} podem montar um triangulo! Vamos classificalo agora: ')
    if l1 == l2 == l3:
        print(f'É um triângulo Equilátero!')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print(f'É um triângulo Isósceles')
    else:
        print(f'É um triângulo Escaleno!')
else:
    print('Não é possível formar um triângulo!')