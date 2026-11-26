import sys
from itertools import combinations

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    n = int(d[0])
    k = int(d[1])
    raw = d[2:2 + n]
    names = sorted(list(set(raw)))
    for c in combinations(names, k):
        print(' '.join(c))

if __name__ == '__main__':
    solve()