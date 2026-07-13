import math

def nto(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    demnto = 0
    demkonto = 0
    for c in n:
        if nto(int(c)): demnto += 1
        else: demkonto += 1
    if nto(len(n)) and demnto > demkonto:
        print("YES")
    else:
        print("NO")