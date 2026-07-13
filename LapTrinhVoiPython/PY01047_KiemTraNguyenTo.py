import math


def nto(n):
    if n < 2: return False
    for i in range (2, math.isqrt(n)+1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range(t):
    s = input()
    ok = False
    for j in range(len(s)):
        if (nto(int(s[len(s) - 4:len(s)]))) :
            ok = True
            break
    if ok:
        print('YES')
    else:
        print('NO')