import sys

def solve_hex_fast(A):
    tot = sum(A)
    if tot % 3 != 0:
        return 0
    S = tot // 3
    val_to_mask = {}
    for i, v in enumerate(A):
        val_to_mask[v] = val_to_mask.get(v, 0) | (1 << i)
    quads = [[] for _ in range(12)]
    by_ac = {}
    by_ad = {}
    for a in range(12):
        va = A[a]
        ma = 1 << a
        for b in range(12):
            if b == a:
                continue
            vb = A[b]
            mb = ma | (1 << b)
            for c in range(12):
                if (mb >> c) & 1:
                    continue
                vc = A[c]
                mc = mb | (1 << c)
                vd = S - va - vb - vc
                md_avail = val_to_mask.get(vd, 0) & ~mc
                while md_avail:
                    low = md_avail & -md_avail
                    d = low.bit_length() - 1
                    m = mc | low
                    quads[a].append((b, c, d, m))
                    k_ac = (a, c)
                    if k_ac not in by_ac:
                        by_ac[k_ac] = []
                    by_ac[k_ac].append((b, d, m))
                    k_ad = (a, d)
                    if k_ad not in by_ad:
                        by_ad[k_ad] = []
                    by_ad[k_ad].append((b, c, m))
                    md_avail ^= low
    ans = 0
    for t0 in range(12):
        for r0, r1, t2, m_l1 in quads[t0]:
            for r5, r4, t4, m_l2 in quads[t0]:
                if (m_l1 & m_l2) != (1 << t0):
                    continue
                m12 = m_l1 | m_l2
                for r2, r3, m_l3 in by_ad.get((t2, t4), ()):
                    if m_l3 & (m12 ^ (1 << t2) ^ (1 << t4)):
                        continue
                    m123 = m12 | m_l3
                    for t1, t3, m_l4 in by_ac.get((r1, r2), ()):
                        if m_l4 & (m123 ^ (1 << r1) ^ (1 << r2)):
                            continue
                        m1234 = m123 | m_l4
                        rem_t5 = 4095 ^ m1234
                        t5 = rem_t5.bit_length() - 1
                        if A[t1] + A[r0] + A[r5] + A[t5] == S and A[t3] + A[r3] + A[r4] + A[t5] == S:
                            ans += 1
    return ans // 12

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        A = [int(x) for x in data[idx:idx + 12]]
        idx += 12
        out.append(str(solve_hex_fast(A)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()