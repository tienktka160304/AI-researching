def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))     #[1]
print(f(2))     #[2]
print(f(3))     #[3]
