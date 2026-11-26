import sys
from heapq import heappush, heapreplace

toks = list(map(int, sys.stdin.read().split()))
if toks:
    n = toks[0]
    a = toks[1 : 1 + n]
    h = []
    ans = 0
    for i, x in enumerate(a):
        v = x - i
        heappush(h, -v)
        if -h[0] > v:
            ans += -h[0] - v
            heapreplace(h, -v)
    print(ans)