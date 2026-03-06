#Conversor de real para dólar
dol = 5.35
real = float(input('Quantos reais você quer converter? R$'))
conv = real / dol

print(f'R${real:.2f} equivale a USD {conv:.2f}')
