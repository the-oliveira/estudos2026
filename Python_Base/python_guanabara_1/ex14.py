#Algoritmo que mostre o preço de um produto e o preço com um desconto de 5%
produto = float(input('Qual o valor do produto? R$'))
desconto = produto - (produto * 0.05)

print(f'O produto custa R${produto:.2f} se o pagamento for no pix, terá o deconto de 5%, ficando R${desconto:.2f}')