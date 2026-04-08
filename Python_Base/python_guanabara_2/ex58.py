#Programa lê o sexo de uma pessoa
#Aceita só M ou F, faça o laço até ser True
p_sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]

while p_sexo not in 'MF' or p_sexo == '':
    p_sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()

if p_sexo == 'M':
    print('Dado validado com sucesso: Masculino')
else:
    print('Dado validado com sucesso: Feminino')