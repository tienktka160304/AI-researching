for n in range(2, 15):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n//x)
            break
    else:
       print(n, " prime")
# 2  prime
# 3  prime
# 4 = 2 * 2
# 5  prime
# 6 = 2 * 3
# 7  prime
# 8 = 2 * 4
# 9 = 3 * 3
# 10 = 2 * 5
# 11  prime
# 12 = 2 * 6
# 13  prime
# 14 = 2 * 7