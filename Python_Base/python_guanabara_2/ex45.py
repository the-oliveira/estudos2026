#Recebe o preço do produto e considera o valor total de acordo com o metodo de pagamento:
#PIX = 10% de desconto
#Cartão a vista = 5% de desconto
#Em 2x no cartão = preço normal
#Em 3x ou mais = 20% de juros
from time import sleep

preco_produto = float(input('Qual o preço do produto? R$'))

print(f'O produto custa R${preco_produto:.2f}, deseja pagar como?')
sleep(1)
print('''

[1] PIX (10% de desconto)
[2] Cartão à vista (5% de desconto)
[3] Cartão (Até 2x sem juros)

''')
sleep(2)
escolha = int(input('Escolha uma das opções: '))
sleep(1)
if escolha == 1:
    sleep(1)
    print('Um desconto de 10% será aplicado ao produto!')
    sleep(1)
    print(f'O valor total a ser pago é de R${preco_produto - (preco_produto * 0.10):.2f}')
    sleep(1)
elif escolha == 2:
    sleep(1)
    print('Um desconto de 5% será aplicado ao produto!')
    sleep(1)
    print(f'O valor total a ser pago é de R${preco_produto - (preco_produto * 0.05):.2f}')
    sleep(1)
elif escolha == 3:
    sleep(1)
    print('Pagamentos com cartão até 2x sem juros e no maximo 12x com 20% de juros.')
    sleep(1)
    parcela_escolha = int(input('Deseja pagar em quantas vezes? '))
    sleep(1)
    if parcela_escolha > 2:
        sleep(1)
        total_juros = preco_produto + (preco_produto * 0.20)
        sleep(1)
        print('Juros de 20% aplicado ao valor total!')
        sleep(1)
        print(f'O valor total a ser pago é de R${total_juros:.2f}')
        sleep(1)
        print(f'Em {parcela_escolha}x de R${total_juros / parcela_escolha:.2f}')
        sleep(1)
    elif parcela_escolha == 2:
        sleep(1)
        print(f'O valor total a ser pago é de R${preco_produto:.2f}')
        sleep(1)
        print(f'Em {parcela_escolha}x de R${preco_produto/parcela_escolha:.2f}')
        sleep(1)
    else:
        sleep(1)
        print('Para pagamentos em 1x, escolha a opção no menu anterior... Obrigado!')
        sleep(1)
else:
    sleep(1)
    print('Escolha uma opção válida!')
    sleep(1)