#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Coletando dados do cliente
diasAlugados = int(input('Quantos dias o carro ficou alugado? '))
kmRodados = float(input('Quantos KM o carro rodou? '))

#Total final
precoDia = 60 * diasAlugados
precoKm = kmRodados * 0.15

print(f'Você alugou o carro por {diasAlugados} e rodou {kmRodados}KM, o total do aluguel foi de R${precoDia + precoKm:.2f}.')