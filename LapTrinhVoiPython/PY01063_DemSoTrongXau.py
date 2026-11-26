import sys

def solve():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    idx = 1
    for _ in range(t):
        s = d[idx]
        n = d[idx + 1]
        idx += 2
        print(s.count(n))

if __name__ == '__main__':
    solve()