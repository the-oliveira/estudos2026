#Programa que recebe altura e largura de uma parede em metros e calcula a área e a quantidade de tinta necessária para pintar a parede
#Cada litro de tinta pinta uma área de 2m²

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = altura * largura
tintaNecessaria = area / 2


print(f'Para sua parede de {altura:.2f}m de altura e {largura:.2f}m de largura, temos o total de {area:.2f}m² de área')
print(f'A quantidade de tinta necessária será {tintaNecessaria:.2f} litros')