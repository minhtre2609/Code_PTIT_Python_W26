import math

def nto(n):
    if n < 2 : return False
    for i in range (2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    cnt = 0
    for i in range(1, n):
        if (math.gcd(i, n) == 1):
            cnt += 1

    if nto(cnt): print('YES')
    else: print('NO')