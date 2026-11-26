import sys

def solve():
    line0 = sys.stdin.readline()
    while line0 and not line0.strip():
        line0 = sys.stdin.readline()
    if not line0:
        return
    n = int(line0.strip())
    row0 = []
    while len(row0) < n:
        row0.extend(int(x) for x in sys.stdin.readline().split())
    if n == 2:
        val = row0[1]
        print(val // 2, val - val // 2)
        return
    row1 = []
    while len(row1) < n:
        row1.extend(int(x) for x in sys.stdin.readline().split())
    b01 = row0[1]
    b02 = row0[2]
    b12 = row1[2]
    a0 = (b01 + b02 - b12) // 2
    res = [a0] + [row0[i] - a0 for i in range(1, n)]
    print(*(res))

if __name__ == '__main__':
    solve()