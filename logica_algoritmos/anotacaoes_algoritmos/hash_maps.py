#Anotações do padrão HASH MAP

'''
Quando preciso salvar uma chave para acessar um valor especifico

- o poder do hash map é você poder acessar um valor simplesmente passando a chave 
- a resposta é imediata e independe do tamanho do dicionario
- chaves precisam ser numeros, strings ou tuplas
- Util para achar valores que já foram acessados em um loop

O padrão segue essa estrutura:

1 - Armazena uma informação
    - caso o item não esteja no hash_map
2 - Procura por algo (condição)
    - Verifica se o valor já passou pelo loop (verifica o mapa)
3 - Update ou inicia valores
    - caso queira incrementar o valor se ele já estava no hash_map

Se você pode responder a pergunta: 
Consigo armazenar algo para não ter que realizar força bruta?
Então da para usar Hash Map para destravar a solução.

'''
#Exemplo:

list_nums = [0, 1, 22, 33, 23, 2, 4]
hash_map = dict() #Iniciando o mapa

for n in list_nums: #Iniciando o loop
    if n not in hash_map:
        hash_map[n] = 1 #Adicionando o valor visto pela primeira vez ao mapa
    else:
        hash_map[n] += 1 #Incrementando o valor que já foi visto




