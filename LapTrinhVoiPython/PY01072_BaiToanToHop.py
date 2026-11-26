import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k = int(data[0]), int(data[1])
    vals = sorted(set(int(x) for x in data[2:2 + n]))
    for comb in combinations(vals, k):
        sys.stdout.write(" ".join(map(str, comb)) + "\n")

solve()