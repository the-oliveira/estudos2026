#Programa lê 2 valores e mostra um menu:
#Fazer um menu com: soma, multiplicação, maior número, novos números ou sair do programa
from time import sleep

op_menu = 1

print('=' * 30)
primeiro_num = int(input('Digite o primeiro valor: '))
segundo_num = int(input('Digite o segundo valor: '))
print('=' * 30)
sleep(1)

while op_menu != 0:

    print(f'{' ESCOLHA UMA OPÇÃO ':=^30}')
    print('''

    [1] - SOMA
    [2] - MULTIPLICAÇÃO
    [3] - MAIOR NÚMERO
    [4] - TROCAR NÚMEROS
    [0] - SAIR
        
    ''')
    print('='*30)

    op_menu = int(input('Opção desejada: '))

    if op_menu > 4 or op_menu < 0:
        sleep(1)
        print(f'[ERRO] - {op_menu} Não é um valor válido!')
        sleep(1)
    elif op_menu == 1:
        print('Vamos somar os valores!')
        sleep(1)
        soma = primeiro_num + segundo_num
        print(f'A soma de {primeiro_num} + {segundo_num} = {soma}')
        sleep(5)
    elif op_menu == 2:
        print('Vamos multiplicar os valores!')
        sleep(1)
        multi = primeiro_num * segundo_num
        print(f'A multiplicação de {primeiro_num} x {segundo_num} = {multi}')
        sleep(5)
    elif op_menu == 3:
        print('Vamos analisar qual o maior número...')
        sleep(1)
        if primeiro_num > segundo_num:
            print(f'O maior número é o {primeiro_num}')
        elif segundo_num > primeiro_num:
            print(f'O maior número é o {segundo_num}')
        else:
            print(f'Os valores são iguais!')
        
        sleep(5)
    elif op_menu == 4:
        sleep(1)
        print('Iniciando troca de valores...')
        sleep(1)
        primeiro_num = int(input('Digite o primeiro número: '))
        segundo_num = int(input('Digite o segundo número: '))
        sleep(5)
