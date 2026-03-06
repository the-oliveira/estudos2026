#Algoritmo que receba o salário de um funcionario e adicione um aumento de 15%
salario = float(input('Qual o seu salario atual? R$'))
aumento = salario + (salario * 0.15)

print(f'Seu salário de R${salario:.2f} agora foi reajustado para R${aumento:.2f}, ou seja, 15% de aumento!')