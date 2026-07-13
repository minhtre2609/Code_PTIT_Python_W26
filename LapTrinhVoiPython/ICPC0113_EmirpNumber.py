import math

def nto(n):
    if n < 2 : return False
    for i in range (2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def dao_so(n):
    dao = str(n)[::-1]
    return int(dao)

t = int(input())
for i in range(t):
    n = int(input())
    for i in range(2, n):
        rev = dao_so(i)
        if rev < n and rev != i and i < rev and nto(i) and nto(rev):
            print(i, rev, end = " ")
    print()