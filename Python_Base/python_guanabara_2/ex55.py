#Programa recebe 7 anos de nascimentos e diz quantas são maiores de idades e quantas ainda não são.
from datetime import date

hoje = date.today().year
maiores = 0
menores = 0

for n in range (1, 8):
    dt_nasc = int(input(f'Ano de nascimento da {n} pessoa? '))
    if hoje - dt_nasc < 18:
        menores += 1
    elif hoje - dt_nasc >= 18:
        maiores += 1

print(f'''

Entre as datas informadas temos {maiores} pessoas MAIORES de idade
Entre as datas informadas temos {menores} pessoas MENORES de idade

''')