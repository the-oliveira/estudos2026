#x = 121 #True
x = -121 #False
#x = 10 #false

x = str(x)
ini = 0
end = len(x) - 1

while ini <= end:
    if x[ini] != x[end]:
        print('False')
        break
    
    else:
        ini += 1
        end -= 1

print('True')