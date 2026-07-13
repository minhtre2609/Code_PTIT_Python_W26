import math


def nto(n):
    if n < 2: return False
    for i in range (2, math.isqrt(n)+1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range(t):
    n = input()
    tong = 0
    for c in n:
        tong += int(c)
    if (nto(tong)): print("YES")
    else: print("NO")