import sys

def solve_2080_fast(n, m, s):
    if m == 1:
        return 0
    k = len(s)
    if n < k:
        return 0
    c = [0] * (k + 1)
    c[0] = 1
    c[1] = -26
    for j in range(1, k):
        if s[:k - j] == s[j:]:
            c[j] += 1
            c[j + 1] -= 26
    c[k] += 1
    deg = k
    char_tail = [(-c[deg - i]) % m for i in range(deg)]

    def combine(P, Q):
        R = [0] * (2 * deg - 1)
        for i, p in enumerate(P):
            if p:
                for j, q in enumerate(Q):
                    if q:
                        R[i + j] += p * q
        for d in range(2 * deg - 2, deg - 1, -1):
            v = R[d] % m
            if v:
                base = d - deg
                for i in range(deg):
                    R[base + i] += v * char_tail[i]
        return [R[i] % m for i in range(deg)]

    init = [pow(26, i, m) for i in range(deg)]
    res = [0] * deg
    res[0] = 1
    base = [0] * deg
    if deg > 1:
        base[1] = 1
    else:
        base[0] = char_tail[0]
    p = n
    while p > 0:
        if p & 1:
            res = combine(res, base)
        base = combine(base, base)
        p >>= 1
    bad = sum(res[i] * init[i] for i in range(deg)) % m
    return (pow(26, n, m) - bad) % m

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        out.append(str(solve_2080_fast(n, m, s)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()