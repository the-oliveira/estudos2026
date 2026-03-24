#Programa recebe a distancia de uma viagem em KM
#Vai calcular o preço da passagem 
#Caso a viagem seja de até 200km, será 0,50 centavos por KM
#Acima disso, será 0,45 centavos por KM
viagem_km = int(input('Qual a distância da viagem em KM? '))

if viagem_km <= 200:
    print(f'A distância da viagem é de {viagem_km}KM, então irá custar R${viagem_km * 0.50:.2f}')
else:
    print(f'A distância da viagem é de {viagem_km}KM, então irá custar R${viagem_km * 0.45:.2f}')