import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    inf = 1000000
    for _ in range(t):
        n = int(raw[ptr])
        m = int(raw[ptr + 1])
        k = int(raw[ptr + 2])
        ptr += 3
        grid = raw[ptr : ptr + n]
        ptr += n
        c0 = [-1] * m
        c1 = [-1] * m
        c2 = [-1] * m
        c3 = [-1] * m
        c4 = [-1] * m
        ans = 0
        base_left = [i - 1 for i in range(m)]
        for b in range(n):
            row = grid[b]
            left_link = base_left[:]
            for r in range(m):
                if row[r] == '1':
                    c4[r] = c3[r]
                    c3[r] = c2[r]
                    c2[r] = c1[r]
                    c1[r] = c0[r]
                    c0[r] = b
                if k == 4:
                    t0, t1, t2, t3, t4 = c0[r], c1[r], c2[r], c3[r], c4[r]
                elif k == 3:
                    t0, t1, t2, t3, t4 = inf, c0[r], c1[r], c2[r], c3[r]
                elif k == 2:
                    t0, t1, t2, t3, t4 = inf, inf, c0[r], c1[r], c2[r]
                else:
                    t0, t1, t2, t3, t4 = inf, inf, inf, c0[r], c1[r]
                c = r
                while True:
                    prv = left_link[c]
                    while prv >= 0 and c0[prv] <= t4:
                        prv = left_link[prv]
                    left_link[c] = prv
                    if t3 > t4:
                        ans += (t3 - t4) * (c - prv)
                    if prv < 0:
                        break
                    c = prv
                    x = c0[c]
                    if x >= t0:
                        t4 = t3; t3 = t2; t2 = t1; t1 = t0; t0 = x
                    elif x >= t1:
                        t4 = t3; t3 = t2; t2 = t1; t1 = x
                    elif x >= t2:
                        t4 = t3; t3 = t2; t2 = x
                    elif x >= t3:
                        t4 = t3; t3 = x
                    else:
                        t4 = x
                    x = c1[c]
                    if x > t4:
                        if x >= t1:
                            t4 = t3; t3 = t2; t2 = t1; t1 = x
                        elif x >= t2:
                            t4 = t3; t3 = t2; t2 = x
                        elif x >= t3:
                            t4 = t3; t3 = x
                        else:
                            t4 = x
                        x = c2[c]
                        if x > t4:
                            if x >= t2:
                                t4 = t3; t3 = t2; t2 = x
                            elif x >= t3:
                                t4 = t3; t3 = x
                            else:
                                t4 = x
                            x = c3[c]
                            if x > t4:
                                if x >= t3:
                                    t4 = t3; t3 = x
                                else:
                                    t4 = x
                                x = c4[c]
                                if x > t4:
                                    t4 = x
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

solve()