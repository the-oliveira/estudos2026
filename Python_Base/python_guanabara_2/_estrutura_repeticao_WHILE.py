#Anotações da aula sobre WHILE

#While é utilizado para laços onde não se sabe o limite (final desconhecido)
#Estrutura de repetição com teste lógico
#Repete o loop enquanto a condição for verdadeira

soma = 0

while soma <= 100:
    num = int(input('Digite um número: '))
    soma += num
print(f'Fim! a soma chegou a {soma}')