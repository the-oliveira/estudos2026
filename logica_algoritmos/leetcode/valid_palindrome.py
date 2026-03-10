s = "A man, a plan, a canal: Panama" #True
#s = "race a car"                   #False
#s = " "                            #True

start = 0
end = len(s) - 1
s = s.lower() #Passando o texto para lower


while start <= end:
    while start < end and not s[start].isalnum(): #Rodando o loop até encontrar o proximo valor valido para alfanumérico no inicio
        start += 1

    while start < end and not s[end].isalnum(): #Rodando o loop ate encontrar o proximo valor valido para alfanumerico no final
        end -= 1

    if s[start] != s[end]:
        print('False')
        break
    else:
        start += 1
        end -= 1

print('True')