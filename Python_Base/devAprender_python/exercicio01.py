salarioMensal = float(input('Quanto você ganhar por mês? '))
horasDia = int(input('Quantas horas você trabalha por dia? '))
diasTrabalhados = int(input('Quantos dias por mês você trabalha? '))
valorHora = salarioMensal / (horasDia * diasTrabalhados)

print(f'Você ganha R${valorHora:.2f} por hora')