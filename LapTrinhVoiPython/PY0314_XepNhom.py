import sys
from itertools import compress, repeat
from operator import le

readline = sys.stdin.readline
first = readline().split()
if first:
    t = int(first[0])
    out = []
    for _ in range(t):
        line = readline().split()
        while not line:
            line = readline().split()
        n = int(line[0])
        k = int(line[1])
        a = list(map(int, readline().split()))
        while len(a) < n:
            a.extend(map(int, readline().split()))
        total = sum(a)
        d = k
        while True:
            avg = total // d
            if not a or max(a) <= avg:
                break
            n_prev = len(a)
            a = list(compress(a, map(le, a, repeat(avg))))
            d -= n_prev - len(a)
            total = sum(a)
        out.append(str(avg))
        a = None
    sys.stdout.write('\n'.join(out) + '\n')