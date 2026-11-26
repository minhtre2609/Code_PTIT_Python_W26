def prod(x):
    p = 1
    for c in str(x):
        p *= int(c)
    return p

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (prod(x), x))
    print(*a)