#Recebe o nome completo de uma pessoa e printa o primeiro e ultimo nome da pessoa.

nome_completo = str(input('Digite o nome completo: '))
p_nome = nome_completo.split()[0]
ul_nome = nome_completo.split()[-1]

print(f'Primeiro nome: {p_nome}')
print(f'Ultimo nome: {ul_nome}')