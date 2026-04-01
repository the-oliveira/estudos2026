#Lê varios números inteiros 
#Para quando digita 999
#No final, mostrar a quantidade de números digitados e a soma entre eles (desconsiderando o 999)

cont_nums = 0
total_sum = 0
num = int(input('Type a number (999 to stop): '))

while num != 999:
    
    total_sum += num
    cont_nums += 1
    
    num = int(input('Type a number (999 to stop): '))


print(f'Total numbers typed: {cont_nums}')
print(f'The sum of all numbers: {total_sum}')