#Tabuada de um número que o usuário digitar usando o for

num = int(input('Gostaria de saber a tabuada de qual número? '))

for n in range(1, 10+1):
    print(f'{num} x {n:2} = {num * n:2}')