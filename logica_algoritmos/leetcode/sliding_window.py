precos = [7, 1, 5, 3, 6, 4]
compra = 0 
venda = 1 
lucro_maximo = 0

while venda < len(precos):
    
    if precos[venda] < precos[compra]:
        compra = venda
        
    else:
        lucro_do_dia = precos[venda] - precos[compra]
        if lucro_do_dia > lucro_maximo:
            lucro_maximo = lucro_do_dia
            
    venda += 1

print(lucro_maximo)