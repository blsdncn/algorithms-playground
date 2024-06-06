# Tail recursion
def fact2(n, x=1):
    if n == 0:
        return x
    else:
        return fact2(n-1, n*x)