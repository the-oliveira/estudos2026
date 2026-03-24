#Programa de aprovação de emprestimo bancario, vai receber o valor da casa, salário da pessoa e em quantos anos ele irá pagar
#Calculo do programa = para aprovar o valor mensal não pode exceder 30% do salário da pessoa.

#Coletando infos
valor_imovel = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o seu salário? R$'))
parcelas = int(input('Quer pagar em quantos meses? '))

#Calculo das parcelas
valor_parcelas = valor_imovel / parcelas

if valor_parcelas <= salario * 0.30:
    print(f'''
        Empréstimo aprovado!
        O imóvel custa: R${valor_imovel:.2f}
        Valor das parcelas: R${valor_parcelas:.2f}
          ''')
else:
    print(f'''
        Empréstimo recusado!
        O imóvel custa: R${valor_imovel:.2f}
        Valor das parcelas: R${valor_parcelas:.2f}

        A parcela não pode exceder 30% do salário!
''')