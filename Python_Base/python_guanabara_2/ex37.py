#Programa de aprovação de emprestimo bancario, vai receber o valor da casa, salário da pessoa e em quantos anos ele irá pagar
#Calculo do programa = para aprovar o valor mensal não pode exceder 30% do salário da pessoa.

#Coletando infos
valor_imovel = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quer pagar em quantos anos? '))
valor_parcelas = valor_imovel / (anos * 12)

if valor_parcelas <= salario * 0.30:
    print(f'''
        Empréstimo aprovado para o financiamento em {anos} anos!
        O imóvel custa: R${valor_imovel:.2f}
        Valor das parcelas: {anos * 12}x R${valor_parcelas:.2f}

          ''')
else:
    print(f'''
        Empréstimo recusado para o financiamento em {anos} anos!
        O imóvel custa: R${valor_imovel:.2f}
        Valor das parcelas: {anos * 12}x R${valor_parcelas:.2f}

        A parcela não pode exceder 30% do salário!
''')