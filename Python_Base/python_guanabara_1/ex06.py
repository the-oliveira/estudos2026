#Um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele
algo = input('Digite algo: ')

print(f'Você digitou {algo} que é do tipo {type(algo)}')
print(f'{algo} é numérico? {algo.isnumeric()}')
print(f'{algo} é alfa? {algo.isalpha()}')
print(f'{algo} é alfanumerico? {algo.isalnum()}')
print(f'{algo} esta todo em maiusculo? {algo.isupper()}')
print(f'{algo} é um titulo(capitalizado)? {algo.istitle()}')
print(f'{algo} esta todo em minusculo? {algo.islower()}')