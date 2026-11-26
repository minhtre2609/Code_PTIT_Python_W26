import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    if n == 1:
        print("Yes")
        return
    deg = [0] * (n + 1)
    ptr = 1
    for _ in range(n - 1):
        u = int(raw[ptr])
        v = int(raw[ptr + 1])
        deg[u] += 1
        deg[v] += 1
        ptr += 2
    if max(deg) == n - 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()