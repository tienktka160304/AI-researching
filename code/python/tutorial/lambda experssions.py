pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)
#[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
#f > o > t > t


# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# # x = 42
# print(f(0))
# # x = 42 + 0
# print(f(1))
# # x = 42 + 1