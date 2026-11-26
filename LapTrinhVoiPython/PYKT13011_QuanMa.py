import sys

MOD = 1000000007

RECS = {
    1: ([2], [1]),
    2: ([3, 1000000004, 6, 0, 1000000001, 3, 1000000004, 1], [1, 4, 16, 36, 81, 225, 625, 1600]),
    3: ([3, 4, 999999997, 24, 999999929, 999999981, 168, 999999899, 174, 70, 999999631, 144, 999999983, 999999959, 108, 999999971], [1, 8, 36, 94, 278, 1062, 3650, 11856, 39444, 135704, 456980, 1534668, 5166204, 17480600, 58888528, 198548648]),
    4: ([7, 999999997, 13, 999999941, 999999898, 318, 263, 258, 999999690, 999998366, 54, 899, 999999780, 535, 293, 999999838, 140, 14, 999999915, 999999995, 12], [1, 16, 81, 278, 1365, 7164, 33858, 161307, 791722, 3859473, 18702843, 90938441, 442661923, 152542084, 466805502, 911253157, 627500732, 355982144, 651196682, 444225457, 637952710])
}

def solve_knight(m, n):
    rec, init = RECS[m]
    deg = len(rec)
    if n < deg:
        return init[n]
    char_tail = rec[::-1]

    def combine(P, Q):
        R = [0] * (2 * deg - 1)
        for i, p in enumerate(P):
            if p:
                for j, q in enumerate(Q):
                    if q:
                        R[i + j] += p * q
        for d in range(2 * deg - 2, deg - 1, -1):
            v = R[d] % MOD
            if v:
                base = d - deg
                for i in range(deg):
                    R[base + i] += v * char_tail[i]
        return [R[i] % MOD for i in range(deg)]

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
    return sum(res[i] * init[i] for i in range(deg)) % MOD

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        m = int(data[idx])
        n = int(data[idx + 1])
        idx += 2
        out.append(str(solve_knight(m, n)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()