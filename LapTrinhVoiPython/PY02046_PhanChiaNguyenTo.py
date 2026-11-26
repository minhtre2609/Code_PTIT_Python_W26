import sys

def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    d = 5
    while d * d <= x:
        if x % d == 0 or x % (d + 2) == 0:
            return False
        d += 6
    return True

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    seen = set()
    b = []
    for x in a:
        if x not in seen:
            seen.add(x)
            b.append(x)
    tot = sum(b)
    pref = 0
    m = len(b)
    for i in range(m - 1):
        pref += b[i]
        suff = tot - pref
        if is_prime(pref) and is_prime(suff):
            print(i)
            return
    print("NOT FOUND")

solve()