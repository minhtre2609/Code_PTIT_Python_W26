import sys
from itertools import permutations

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    for p in permutations(s):
        sys.stdout.write("".join(p) + "\n")

solve()