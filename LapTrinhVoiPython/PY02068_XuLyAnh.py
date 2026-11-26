import sys
from itertools import accumulate, repeat
from operator import add, sub, floordiv

def solve():
    readline = sys.stdin.readline
    first = readline()
    while first and not first.strip():
        first = readline()
    if not first:
        return
    t = int(first)
    out = []
    for _ in range(t):
        line = readline()
        while line and not line.strip():
            line = readline()
        if not line:
            break
        n, m, l = map(int, line.split())
        l2 = l * l
        w = m - l + 1
        prev = [0] * w
        P = [prev]
        for _ in range(n):
            row = list(map(int, readline().split()))
            while len(row) < m:
                row.extend(map(int, readline().split()))
            p = [0, *accumulate(row)]
            prev = list(map(add, prev, map(sub, p[l:], p)))
            P.append(prev)
        for i in range(n - l + 1):
            out.append(" ".join(map(str, map(floordiv, map(sub, P[i + l], P[i]), repeat(l2)))))
    sys.stdout.write("\n".join(out) + "\n")

solve()