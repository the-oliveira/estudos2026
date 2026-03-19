#Programa lê a velocidade de um carro em km/h
#Se for maior que 80 será Multado
#A multa é de 7 reais a cada KM acima do permitido.

velocidade_carro = int(input('Qual velocidade do carro em KM? '))
multa = (velocidade_carro - 80) * 7.00

if velocidade_carro > 80:
    print(f'Você ultrapassou o limite de 80KM/h e deve pagar R${multa:.2f}')
else:
    print('Parabéns, você está dentro do limite de 80KM/h')