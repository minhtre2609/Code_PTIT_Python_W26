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

def tong_chu_so(n):
    tong = sum(int(i) for i in str(n))
    return tong

def kiem_tra(n):
    s = str(n)
    for i in s:
        digits = int(i)
        if not nto(digits): return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    if nto(n) and nto(dao_so(n)) and nto(tong_chu_so(n)) and kiem_tra(n): print('Yes')
    else: print('No')