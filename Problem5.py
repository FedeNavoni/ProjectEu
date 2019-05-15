Encontrado = False
x = 20
while Encontrado == False:
    i = 0
    for y in range(1, 21):
       if x % y == 0:
           i += 1
    if i == 20:
        Encontrado = True
    else:
        x += 20

print(x)

