#Programa que leia a data de nascimento de um atleta e define a categoria:
#Até 9 anos = mirim, 
#até 14 anos = infantil, 
#até 18 anos = junior, 
#até 20 anos = sênior, 
#acima de 30 = Master
from datetime import datetime

dt_atual = datetime.today().year
dt_nasc = int(input('Em que ano o atleta nasceu? '))
idade = dt_atual - dt_nasc

if idade < 0:
    print(f'[ERRO] {idade} não é um valor válido, digite uma data de nascimento válida!')
elif idade > 0 and idade <= 9:
    print(f'[Categoria Mirim] o atleta possui {idade} anos...')
elif idade > 9 and idade <= 14:
    print(f'[Categoria Infantil] o atleta possui {idade} anos...')
elif idade > 14 and idade <= 18:
    print(f'[Categoria Junior] o atleta possui {idade} anos...')
elif idade > 18 and idade <= 25:
    print(f'[Categoria Sênior] o atleta possui {idade} anos...')
else:
    print(f'[Categoria Master] o atleta possui {idade} anos.')