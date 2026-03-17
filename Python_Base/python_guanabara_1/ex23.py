#Programa recebe o nome completo de uma pessoa e retorna:
#Nome todo maiusculo, 
# Todo minusculo, 
# Tamanho do nome sem espaços, 
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome completo: ')).strip()

print(f'Nome maiusculo: {nome.upper()}')
print(f'Nome minusculo: {nome.lower()}')
print(f'Tamanho do nome sem os espaços: {len(nome.replace(' ', ''))}')
print(f'Tamanho do primeiro nome: {len(nome.split()[0])}')