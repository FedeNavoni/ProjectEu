
a = 1
b = 2
x = 0
fibo = [1, 2]
total = 0
terminos = 2
while x < 4000000:
    x = a + b
    fibo.append(x)
    a = b
    b = x
    terminos += 1
for i in range(0, terminos):
    if fibo[i] % 2 == 0:
        total += fibo[i]
print(total)       
