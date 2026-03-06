#Programa que vai ler um valor em metros e exibe convertido em centimetros e milimetros
valorMetros = float(input('Digite o valor que quer converter: '))
dec = valorMetros * 10
cent = valorMetros * 100
mili = valorMetros * 1000


print(f'{valorMetros}m é equivalente a: ')
print(f'''
{dec:.0f}dm Decimetros, 
{cent:.0f}cm centímetros, 
{mili:.0f}mm Milimetros
''')