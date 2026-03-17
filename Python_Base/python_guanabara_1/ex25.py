#Programa recebe o nome de uma cidade e reconhece se ela inicia ou não com a palavra "Santo"
cidade = str(input('Qual o nome da cidade? '))
inicio = cidade.split()[0].capitalize()

if 'Santo' in inicio:
    print(True)
else:
    print(False)