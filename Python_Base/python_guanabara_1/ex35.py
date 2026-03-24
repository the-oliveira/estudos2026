#Programa recebe o salário de um funcionário e calcula o valor do aumento
#Salarios acima de 1250 = aumento de 10%
#Salario abaixo de 1250 = aumento de 15%

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    print(f'O salário foi reajustado em 10% e agora ganhará R${salario + (salario * 0.10):.2f}')
else:
    print(f'O salário foi reajustado em 15% e agora ganhará R${salario + (salario * 0.15):.2f}')