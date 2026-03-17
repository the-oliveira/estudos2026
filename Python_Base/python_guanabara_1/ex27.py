#Recebe uma frase qualquer e retorna:

#Quantas vezes a letra "A" (independente de ser maiuscula ou minuscula) aparece;
#A posição do primeiro "a" na frase;
#A posição que aparece na ultima vez.

frase = str(input('Digite uma frase: ')).lower().strip()


print(f'Quantas vezes a letra A aparece: {frase.count('a')}')
print(f'A posição que aparece o primeiro A: {frase.find('a') + 1}')
print(f'A posição que aparece o ultimo A: {frase.rfind('a') + 1}')