import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    ptr = 0
    t = int(raw[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(raw[ptr])
        m = int(raw[ptr + 1])
        ptr += 2
        nm = n * m
        a = list(map(int, raw[ptr : ptr + nm]))
        ptr += nm
        target = nm - 1
        if target == 0:
            out.append("0")
            continue
        vis = [0] * nm
        vis[0] = 1
        q = [0]
        step = 0
        ans = -1
        m1 = m + 1
        limit_r = (n - 1) * m
        while q:
            step += 1
            nq = []
            append = nq.append
            for u in q:
                val = a[u]
                if u < limit_r:
                    d = val - a[u + m]
                    if d < 0:
                        d = -d
                    v = u + d * m
                    if d and v < nm and not vis[v]:
                        if v == target:
                            ans = step
                            break
                        vis[v] = 1
                        append(v)
                rem = m - 1 - (u % m)
                if rem:
                    d = val - a[u + 1]
                    if d < 0:
                        d = -d
                    if 0 < d <= rem:
                        v = u + d
                        if not vis[v]:
                            if v == target:
                                ans = step
                                break
                            vis[v] = 1
                            append(v)
                    if u < limit_r:
                        d = val - a[u + m1]
                        if d < 0:
                            d = -d
                        if 0 < d <= rem:
                            v = u + d * m1
                            if v < nm and not vis[v]:
                                if v == target:
                                    ans = step
                                    break
                                vis[v] = 1
                                append(v)
            if ans != -1:
                break
            q = nq
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

solve()