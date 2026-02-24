#Validar se a senha tenha pelo menos 6 caracteres
senhas = ['abc123', 'Abc@123', 'Abc', '123', 'teste123', 202520262024, 2245]

for senha in senhas:
    if len(str(senha)) >= 6:
        print(f'A senha {senha} possui {len(str(senha))} digitos e é valida')
    else:
        print(f'A senha {senha} possui {len(str(senha))} digitos e é invalida')