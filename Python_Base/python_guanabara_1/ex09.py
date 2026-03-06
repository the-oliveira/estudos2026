#Programa para ler as notas de um aluno e mostrar a média
n1 = float(input('Nota no primeiro semestre: '))
n2 = float(input('Nota no segundo semestre: '))
n3 = float(input('Nota no terceiro semestre: '))
n4 = float(input('Nota no quarto semestre: '))
media = (n1 + n2 + n3 + n4) / 4

print(f'As notas foram: {n1}, {n2}, {n3}, {n4}')

if media >= 6:
    print(f'A média final foi {media:.2f}, você está aprovado!')
elif media < 6 and media >= 4:
    print(f'Você ficou de recuperação! Sua média foi {media:.2f}')
else:
    print(f'Sua média foi {media:.2f}, portanto está reprovado!')