#Programa lê o sexo de uma pessoa
#Aceita só M ou F, faça o laço até ser True
p_sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()

while p_sexo not in 'MF' and len(p_sexo) != 1:
    p_sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()

if p_sexo == 'M':
    print('Dado validado com sucesso: Masculino')
else:
    print('Dado validado com sucesso: Feminino')