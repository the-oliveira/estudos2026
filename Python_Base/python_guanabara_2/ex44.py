#Leia o peso e altura de uma pessoa e calcula o IMC
#abaixo de 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal
#entre 25 a 30 sobrepeso
#entre 30 a 40 obesidade
#Acima de 40 obesideade mórbida

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc =  peso / (altura * altura)

if imc < 18.5:
    print(f'O seu IMC é {imc:.2f}, você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC é {imc:.2f}, você está dentro do PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print(f'O seu IMC é {imc:.2f}, você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print(f'O seu IMC é {imc:.2f}, você está com OBESIDADE')
else:
    print(f'O seu IMC é {imc:.2f}, você está com OBESIDADE MÓRBIDA')