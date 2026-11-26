import sys
from math import sqrt

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    s = float(data[0])
    k = 2.0 + sqrt(2.0) + sqrt(6.0)
    r = sqrt(s) / k
    sys.stdout.write(f"{r:.4f}\n")

if __name__ == '__main__':
    solve()