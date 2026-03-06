#Programa que vai ler um valor em metros e exibe convertido em centimetros e milimetros
valorMetros = int(input('Digite o valor que quer converter: (Em metros)'))
cent = valorMetros * 100
mili = valorMetros * 1000


print(f'{valorMetros} metros em centímetros é equivalente a: {cent}cm e milimetros {mili}mm')