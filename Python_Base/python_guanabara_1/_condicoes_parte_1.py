#Anotações da primeira parte da aula de condicionais

#Situações simplificadas da para escrever as condicionais em uma unica linha:
print('Olá' if 1 + 1 == 2 else 'Errado')

nome = str(input('Digite um nome: '))

if nome == 'Ddz': #Se não tem else, é uma condicional simples
    print(f'Salve, {nome}, bom dia!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 5:
    print('Passou!')
else:
    print('Reprovado!') #Quando tem else, é uma condicional composta