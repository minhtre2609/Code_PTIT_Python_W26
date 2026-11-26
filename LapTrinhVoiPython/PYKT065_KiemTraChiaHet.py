import sys
import itertools
import operator
from bisect import bisect_right

def solve():
    M = 510510
    b = bytearray([1]) * M
    for p in (2, 3, 5, 7, 11, 13, 17):
        b[::p] = b'\x00' * ((M + p - 1) // p)
    pref = list(itertools.accumulate(b))
    del b
    TOT = pref[-1]
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    LIMIT = 1000000000000000000
    tables = {}

    def get_table(n):
        t = tables.get(n)
        if t is not None:
            return t
        ps = [p for p in (primes[7:] if n >= 17 else primes) if p <= n]
        terms = [(1, 1)]
        for p in ps:
            terms.extend((d * p, -s) for d, s in list(terms) if d * p <= LIMIT)
        terms.sort()
        pos = [d for d, s in terms if s == 1]
        neg = [d for d, s in terms if s == -1]
        t = (pos, neg)
        tables[n] = t
        return t

    fdiv = operator.floordiv
    mod = operator.mod
    repeat = itertools.repeat
    get_pref = pref.__getitem__
    readline = sys.stdin.readline
    buf = []
    out = []

    def next_tok():
        while not buf:
            line = readline()
            if not line:
                return None
            buf.extend(line.split())
        return buf.pop(0)

    while True:
        s1 = next_tok()
        if s1 is None:
            break
        l = int(s1)
        if l == -1:
            break
        r = int(next_tok())
        n = int(next_tok())
        if l > r:
            out.append("0")
            continue
        l1 = l - 1
        pos, neg = get_table(n)
        kp_r = bisect_right(pos, r)
        kn_r = bisect_right(neg, r)
        kp_l = bisect_right(pos, l1)
        kn_l = bisect_right(neg, l1)
        if n < 17:
            res_r = sum(map(fdiv, repeat(r), pos[:kp_r])) - sum(map(fdiv, repeat(r), neg[:kn_r]))
            res_l = sum(map(fdiv, repeat(l1), pos[:kp_l])) - sum(map(fdiv, repeat(l1), neg[:kn_l]))
        else:
            qpr = list(map(fdiv, repeat(r), pos[:kp_r]))
            qnr = list(map(fdiv, repeat(r), neg[:kn_r]))
            res_r = (sum(map(fdiv, qpr, repeat(M))) - sum(map(fdiv, qnr, repeat(M)))) * TOT + sum(map(get_pref, map(mod, qpr, repeat(M)))) - sum(map(get_pref, map(mod, qnr, repeat(M))))
            qpl = list(map(fdiv, repeat(l1), pos[:kp_l]))
            qnl = list(map(fdiv, repeat(l1), neg[:kn_l]))
            res_l = (sum(map(fdiv, qpl, repeat(M))) - sum(map(fdiv, qnl, repeat(M)))) * TOT + sum(map(get_pref, map(mod, qpl, repeat(M)))) - sum(map(get_pref, map(mod, qnl, repeat(M))))
        out.append(str(res_r - res_l))

    sys.stdout.write("\n".join(out) + "\n")

solve()