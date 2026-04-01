#Lê um número qualquer e faz o fatorial:
#Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Type a number: '))
mult_nums = 1

print(f'{n}! = ', end='')
while n > 0:
    print(f'{n}x', end='')
    mult_nums *= n
    n -= 1

print(f' -> Final result: {mult_nums}')