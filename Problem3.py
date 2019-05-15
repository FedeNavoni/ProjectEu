number = 600851475143
factors = []

for x in range(2, 50000):
    if number % x == 0:
        factors.append(x)
        number = number / x
        x = 2

print(factors)

