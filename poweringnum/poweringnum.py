#To handle the 0 case, just return 1 if n == 0
def power(a, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        half_power = power(a, n // 2)
        return half_power * half_power
    else:
        half_power = power(a, (n - 1) // 2)
        return half_power * half_power * a

base = 3
exponent = 3
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")