def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#def fib_dac(n):
#    if n == 0:
#        return 0
#    F = [[1,1],[1,0]]
#    result = np.power(F)
#    return result

#for i in range(0,5):
#    print(fib_dac(i))

def fib_dp(n,memory={0: 0,1: 1}):
    if n == 0: return memory
    if n in memory:
        return memory[n]
    memory[n] = fib_dp(n-1,memory) + fib_dp(n-2,memory)
    return memory

#This is assuming 0-based indexing
def fib_dp_nd(n,memory=None):
    if memory is None:
        memory = [0,1]
    if len(memory)>=n:
        return memory[:n]
    memory.append(fib_dp_nd(n-1,memory)[len(memory)-2] + fib_dp_nd(n-2,memory)[len(memory)-2])
    return memory[:n]
    
        

print({x:fib_dp_nd(x) for x in range(9)})