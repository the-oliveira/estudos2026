#Lê varios números inteiros e mostra a média entre todos os valores e o maior e menor valor.
#A cada valor digitado deve perguntar ao usuario se ele quer continuar digitando numeros

cont_values = 0
sum_values = 0
max_num = 0
min_num = 0
choice = 'Y'

while choice == 'Y':
    num = int(input('Type a number: '))

    cont_values += 1
    sum_values += num

    if max_num == 0 and min_num == 0:
        max_num = num
        min_num = num
    elif num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

    choice = str(input('Add more numbers? [Y/N]')).strip().upper()[0]
    while choice not in 'YN':
        choice = str(input('Add more numbers? [Y/N]')).strip().upper()[0]


print(f'The sum of all numbers: {sum_values}')
print(f'The avarege of the {cont_values} values: {sum_values/cont_values:.2}')
print(f'The biggest number typed: {max_num}')
print(f'The lowest number typed: {min_num}')