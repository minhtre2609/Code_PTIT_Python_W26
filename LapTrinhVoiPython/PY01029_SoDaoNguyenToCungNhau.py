import math

def dao_so(n):
    dao = str(n)[::-1]
    return int(dao)

t = int(input())
for _ in range(t):
    n = int(input())
    b = dao_so(n)
    if (math.gcd(b, n) == 1):
        print('YES')
    else: print('NO')