import numpy as np
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fib_dac(n):
    if n == 0:
        return 0
    F = [[1,1],[1,0]]
    result = np.power(F)
    return result

for i in range(0,5):
    print(fib_dac(i))