def gcd_function (x, y):
    if (y == 0):
        return x
    else:
        return gcd_function (y, x % y)

a = 54
b = 24
result = gcd_function(a, b)
print(result)
