#Recebe o nome de uma pessoa e reconhece se ela possui "Silva" no nome (em qualquer lugar).

nome = str(input('Nome completo: ')).lower()

if 'silva' in nome:
    print(True)
else:
    print(False)