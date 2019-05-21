import math
Prod = 1
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a**2 + b**2)
        if c / int(c) == 1:
            if a + b + c == 1000:
                A = a
                B = b
                Prod = a*b*c

print(A)
print(B)
print(Prod)
