#Programa lê o nome, idade e sexo de 4 pessoas.
#Mostrar a média de idade
#Nome do homem mais velho
#Quantas mulheres tem menos de 20 anos.

media_idade = 0
hom_mais_velho = ''
hom_idade = 0
mul_menores_vinte = 0
pessoas = 4

for p in range(0, pessoas):
    print('='*35)
    pessoa_nome = str(input(f'Nome da {p+1} pessoa: '))
    pessoa_idade = int(input('Idade da pessoa: '))
    pessoa_sexo = str(input('Sexo da pessoa[homem/mulher]: ')).strip().lower()[0]
    print('='*35)

    media_idade += pessoa_idade #Somando as idades

    if pessoa_sexo == 'h':
        if hom_idade == 0:
            hom_idade = pessoa_idade
            hom_mais_velho = pessoa_nome

        elif pessoa_idade > hom_idade:
            hom_mais_velho = pessoa_nome
            hom_idade = pessoa_idade

    elif pessoa_sexo == 'm':
        if pessoa_idade < 20:
            mul_menores_vinte += 1
    else:
        print('Sexo inválido!')

print(f'''
      
Vamos contabilizar as informações recebidas!

-> Homem mais velho: {hom_mais_velho}
-> Idade do homem mais velho: {hom_idade}
-> Mulheres abaixo de 20 anos: {mul_menores_vinte}
-> Média de idade dos participantes: {media_idade / pessoas}

''')
    
    