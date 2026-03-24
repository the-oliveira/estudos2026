#Programa que vai ler a data de nascimento e dizer se ele deve aguardar para se alistar (menor de 18 anos), se ele deve se alistar (18 anos), ou se já passou o tempo de alistamento(maior que 18)
#Também vai mostrar o tempo que falta para se alistar( em anos) ou quanto tempo já passou.
from datetime import datetime

hoje = datetime.today().year
dt_nasc = int(input('Em que ano você nasceu? '))
idade = hoje - dt_nasc

if idade < 18:
    print(f'Você tem {idade} anos, ainda não está na hora de alistar! Faltam {18 - idade} anos para se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos, você já deve ter se alistado a {idade - 18} anos atrás')
else:
    print(f'Está na hora de se alistar, você tem {idade} anos!')