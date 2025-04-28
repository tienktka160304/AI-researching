def fib(n):         #fib less than n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):        #fib up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b= b, a + b
    return result


fib(2000)           # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
f100 = fib2(100)
print(f100)         #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]