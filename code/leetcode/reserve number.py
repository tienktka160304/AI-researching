def reserve(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reverse = int(str(x_abs)[::-1]) * sign

    if x < -2**31 or x > 2**31 - 1:
        return 0
    return reverse
n = int(input())
print(reserve(n))