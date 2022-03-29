from math import pow, factorial

def poisson(x, lamb):
    return pow(2.71828,-lamb)*pow(lamb,x)/factorial(x)

print(poisson(3,2))
