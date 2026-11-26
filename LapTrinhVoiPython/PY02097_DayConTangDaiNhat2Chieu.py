import sys
from bisect import bisect_left

def solve():
    readline = sys.stdin.readline
    first = readline()
    while first and not first.strip():
        first = readline()
    if not first:
        return
    n = int(first)
    layers_x = []
    layers_y = []
    for _ in range(n):
        line = readline().split()
        while not line:
            line = readline().split()
        x = int(line[0])
        y = int(line[1])
        lo = 0
        hi = len(layers_x)
        while lo < hi:
            mid = (lo + hi) >> 1
            idx = bisect_left(layers_x[mid], x) - 1
            if idx >= 0 and layers_y[mid][idx] < y:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(layers_x):
            layers_x.append([x])
            layers_y.append([y])
        else:
            xs = layers_x[lo]
            ys = layers_y[lo]
            pos = bisect_left(xs, x)
            if pos > 0 and ys[pos - 1] <= y:
                continue
            if pos < len(xs) and xs[pos] == x and ys[pos] <= y:
                continue
            end = pos
            m = len(ys)
            while end < m and ys[end] >= y:
                end += 1
            xs[pos:end] = [x]
            ys[pos:end] = [y]
    print(len(layers_x))

solve()