print("Ingrese un numero:")
x = 100

sumsqrt = (x*(x+1)*(2*x+1))/6

sqrtsum = (x*(x+1))/2

print("The sum of the squares is:")
print(sumsqrt)
print("The square of the suam is:")
print(sqrtsum**2)

print("The difference between the sum of the squares and the square of the sum is:")
result = sqrtsum**2 - sumsqrt
print(result)

