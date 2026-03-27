#Laço de repetição FOR

#for p in range(0,10) -> in range delimita o intervalo de um laço for
#a contagem não inclui o ultimo item do intervalo (nesse caso o 11)
for p in range(0, 11):
    print(p)

print('='*20)

#para contar de trás para frente basta adicionar o -1 no range
for p in range(6, 0, -1):
    print(p)

print('='*20)

#Se colocar um número após a virgula sem ser o -1 ele irá realizar a contagem de X em X
for p in range(0, 10, 2): #Nesse caso pulando de 2 em 2 excluindo o 10 (por ser o ultimo)
    print(p)

print('='*20)