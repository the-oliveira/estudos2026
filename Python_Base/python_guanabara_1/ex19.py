#Comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#Calcule e mostre o comprimento da hipotenusa
cateto_op = float(input('Digite o cateto oposto: '))
cateto_adj = float(input('Digite o cateto adjacente: '))
hipotenusa = (cateto_op ** 2 + cateto_adj ** 2) ** (1/2)

print(f'A hipotenusa vai medir: {hipotenusa:.2f}')