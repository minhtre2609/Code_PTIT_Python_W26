import sys

def count_oriented(x, y):
    res = 0
    for a in range(1, min(x // 2, y) + 1):
        res += (x - 2 * a + 1) * (y - a + 1)
    for a in range(2, min(x - 1, y) + 1):
        k = min(a - 1, x - a)
        if k > 0:
            sum_b = k * (x - a + 1) - k * (k + 1) // 2
            res += 2 * (y - a + 1) * sum_b
    return res

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        ans = 0
        for d in range(1, min(x, y) + 1):
            ans += 4 * (x - d + 1) * (y - d + 1)
        ans += 2 * count_oriented(x, y) + 2 * count_oriented(y, x)
        out.append(str(ans))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()