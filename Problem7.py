Contador = 0
Numero = 1 
while Contador != 10001:
    Numero += 1
    cont_div = 0
    for i in range(1, Numero + 1):
        if Numero % i == 0:
            cont_div += 1
        if cont_div > 2:
            break
    if cont_div == 2:
        Contador += 1

print(Numero)
