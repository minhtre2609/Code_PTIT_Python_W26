import sys
from math import hypot, pi, sin, atan2

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    a = float(data[0])
    b = float(data[1])
    if a > b:
        a, b = b, a
    c = hypot(a, b)
    r = (a + b - c) / 2.0
    theta = atan2(a, b)
    s = sin(theta / 2.0)
    q = (1.0 - s) / (1.0 + s)
    tot_r2 = r * r / (1.0 - q * q)
    area_tri = 0.5 * a * b
    sys.stdout.write(f"{pi * tot_r2 / area_tri:.4f}\n")

if __name__ == '__main__':
    solve()