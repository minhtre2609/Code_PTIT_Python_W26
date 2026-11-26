import sys

def count_digits(n):
    if n <= 0:
        return [0] * 10
    counts = [0] * 10
    pos = 1
    while pos <= n:
        higher = n // (pos * 10)
        cur = (n // pos) % 10
        lower = n % pos
        for d in range(1, 10):
            if cur < d:
                counts[d] += higher * pos
            elif cur == d:
                counts[d] += higher * pos + lower + 1
            else:
                counts[d] += (higher + 1) * pos
        if higher > 0:
            if cur == 0:
                counts[0] += (higher - 1) * pos + lower + 1
            else:
                counts[0] += higher * pos
        pos *= 10
    return counts

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    t = int(raw[0])
    ptr = 1
    out = []
    for _ in range(t):
        a = int(raw[ptr])
        b = int(raw[ptr + 1])
        ptr += 2
        cb = count_digits(b)
        ca = count_digits(a - 1)
        res = [cb[i] - ca[i] for i in range(10)]
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()