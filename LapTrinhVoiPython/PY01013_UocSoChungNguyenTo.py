import math

def nto(n):
    if n < 2: return False
    for i in range (2, math.isqrt(n)+1):
        if (n % i == 0): return False
    return True

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    if nto(g):
        print('YES')
    else:
        print('NO')
