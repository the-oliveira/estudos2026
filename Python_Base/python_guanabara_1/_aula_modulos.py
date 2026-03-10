#Aula de módulos
#Comando import para importar os módulos
#usar o from para puxar as funcionalidades que precisa, sem precisar importar o módulo inteiro

from math import sqrt #Importando funcionalidades sem o módulo inteiro tira a necessidade de chamar o módulo na hora de usar
import random #Gera números aleatórios
import emoji #Adiciona emojis

num = int(input('Digite um número: '))
raiz = sqrt(num) #Chamando método sem nomear o módulo antes

print(f'A raiz de {num} é: {raiz:.2f}')
print(emoji.emojize(":sunglasses:"))

num_random = random.randint(0, 99999999999999999) #Gera um número aleatório inteiro na range informada
print(num_random)
