#Anotações da aula de manipulação de strings

#Fatiamento: Cortar trechos de uma string
frase = 'Salve o Corinthians!'
print(frase[0:3])               #Colocando um recorte de uma parte da string, onde o 0 é o inicio e o 3 é o (fim - 1) (exclui o delimitador 3)
print(frase[0:12:2])            #A terceira casa é o 'passo', ou seja, vai saltar de 2 em 2 do indice 0 ao 12 (excluindo 12)
print(frase[:5])                #Deixando o numero após o : ele vai pegar do inicio até o indice 5.
print(frase[12:])               #Deixando o número antes do : ele vai pegar do 12 até o final da sstring.
print(frase[2::3])              #Deixando 2 :: no meio significa que vai do indice 2 até o final pulando de 3 em 3.

print(len(frase))               #Para ver o tamanho da string.
print(frase.count('a'))         #Conta quantas vezes a letra aparece na string (É case sensitive)
print(frase.count('o', 0, 13))  #Conta quantas vezes a letra em aspas é encontrada no intevalo de 0 a 13 (excluindo o 13)

print(frase.find('Salve'))      #Retornara a posição que essa frase começa na string, Se não existir ele retornara -1

if 'Corinthians' in frase:      #Para verificar se existe o texto entre aspas em uma string da para usar o IN em um IF
    print('Sim')

frase.replace('Salve', 'Vai')   #Troca a palavra da primeira aspas, no caso 'Salve', para a palavra da segunda aspas, 'Vai'

#Para transformar a string em tudo maiusculo 
frase.upper()

#Para transformar a string em tudo minusculo
frase.lower()

#Para transformar o primeiro caractere em maiusculo
frase.capitalize()

#Para deixar a primeira letra de cada palavra em maiusculo
frase.title()

#Se quiser remover os espaços de uma string no inicio e no final
frase.strip()
frase.rstrip() #Remove os espaços a direita da string (final)
frase.lstrip() #Remove os espaços a esquerda da string (inicio)


#Dividir strings:
frase.split() #Divide a string considerando os espaços e cria uma lista com cada palavra.

'-'.join(frase) #Vai unificar as strings da lista utilizando o separador em aspas antes do .join

#Printar strings em mais de uma linha:
print('''
Assim o print vai sair
em mais de uma linha''')

#Strings são imutaveis, não da para alterar o que está escrita a menos que você reatribua o valor da variavel com a mudança ou crie uma nova variavel com a informação dessa string alterada.