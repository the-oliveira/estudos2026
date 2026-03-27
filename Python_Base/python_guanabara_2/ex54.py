#Programa que lê uma frase qualquer e verifica se é um palindromo desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().lower()
ini = 0
fim = len(frase)
palindromo = True

for l in frase:
    if frase[ini] == ' ':
        ini += 1
    elif frase[fim - 1] == ' ':
        fim -= 1
    elif frase[ini] == frase[fim-1]:
        ini += 1
        fim -= 1
    else:
        palindromo = False

if palindromo == True:
    print(f'A frase "{frase}" é um palindromo!') 
else:
    print(f'A frase "{frase}" não é um palindromo!')
        