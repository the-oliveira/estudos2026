#Arrays
'''
Arrays are stored with indexes starting from 0.
You can access the value of one position with O(1) if you type arr[position]

to insert or deleting a value in the middle we move everything to fill the gap O(n)
append value = O(1) 

Em entrevistas:
- atravessar listas ordenadas
- acessar indices de uma lista
- comparar elementos
- da pra usar em algoritmos de sliding window e prefix sum.

'''

#Strings

'''
Strings are array of char

If you need to create a string in a for loop, the correct is use a list,
you append the char to this list and after the for loop, just use "".join(list)
This is O(n)

Em entrevistas:

-Achar a maior substring sem repetir os caracteres
-checar se duas strings são anagramas
-retornar todas as substrings que possuem certo padrão

'''

#Set

'''
Collection of unic values (do not allow duplicates)
a set is define like this: set = {a, b, c, d}

If we want to find a value in a list, coverting this list to a set(list) allows
to use this command, for example if you want to find number 3 in the list:

seen = set(list)
return 3 in seen <- This will return True or False in O(1)

Em entrevistas:

- Usar em problemas que devo verificar se existem valores duplicados
- Em problemas onde preciso gravar o que eu já vi antes
- Validar problemas onde preciso encontrar o primeiro elemento que repete na lista
- Sliding window -> para ver quais valores são unicos

'''

#Control flow and Looping

'''
Quase todos os problemas em entrevistas possuem essas 3 caracteristicas:

    - Um loop
    - Uma condição
    - Variaveis sendo atualizadas

'''

#BIG O Notation

'''
Efficiency of running the Algorithm based on input size

O(1) -> Constante, independente do tamanho do input
    - Verificar se um valor está em um Set
    - Acessar um index de um array

O(log n) -> Divide o problema pela metade em cada execução
    -Binary Search

O(n) -> Tempo linear, cresce baseado no tamanho da lista
    -Atravessa a lista uma vez em um loop

O(n log n) -> Ordenação de listas

O(n²) -> loops aninhados (força bruta)

'''