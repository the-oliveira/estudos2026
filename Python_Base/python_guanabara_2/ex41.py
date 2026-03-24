#Programa recebe 4 notas, se for abaixo de 5 = reprovado, entre 5 e 6.9 = recuperação, maior igual a 7 = aprovado;
n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))
n3 = float(input('Nota do terceiro bimestre: '))
n4 = float(input('Nota do quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4

if media < 5:
    print(f'[REPROVADO] Sua média foi {media:.2f}, não foi suficente para passar!')
elif media >= 5 and media < 7:
    print(f'[RECUPERAÇÃO] Você ficou com {media:.2f} de média, terá uma nova chance na recuperação!')
else:
    print(f'[APROVADO] Você ficou com {media:.2f} de média, portanto está aprovado! Boas férias!')