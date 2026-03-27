#Programa lê o peso de 5 pessoas e mostra o maior e o menor.
maior = 0.0
menor = 0.0

for n in range(1, 6):
    peso = float(input('Digite o peso da pessoa em KG: '))
    if n == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    
print(f'''
      
Dentre as pessoas temos:

Maior peso: {maior}KG
Menor peso: {menor}KG      

''')