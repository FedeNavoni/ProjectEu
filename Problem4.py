
palindromic = []

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        number = x*y
        digitos = len(str(number))
        if str(number)[0] == str(number)[digitos -1] and str(number)[1] == str(number)[digitos -2] and str(number)[2] == str(number)[digitos -3]:
            palindromic.append(number)

print(palindromic)
print(max(palindromic))
