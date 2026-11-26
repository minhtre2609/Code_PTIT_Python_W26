def solve():
    tokens = []
    try:
        while True:
            tokens.extend(input().split())
    except EOFError:
        pass
    if not tokens:
        return

    idx_tok = 0
    t = int(float(tokens[idx_tok]))
    idx_tok += 1
    alpha = 0.000123456789
    eps = 1e-9

    for _ in range(t):
        if idx_tok + 1 >= len(tokens):
            break
        n = int(float(tokens[idx_tok]))
        k = int(float(tokens[idx_tok + 1]))
        idx_tok += 2
        pts = []
        for _ in range(n):
            if idx_tok + 1 >= len(tokens):
                break
            pts.append((float(tokens[idx_tok]), float(tokens[idx_tok + 1])))
            idx_tok += 2

        pts = list(dict.fromkeys(pts))
        m_pts = len(pts)
        if k < 0 or k > m_pts - 3:
            print("NO")
            continue

        rpts = [
            (x + alpha * y, y - alpha * x, i) for i, (x, y) in enumerate(pts)
        ]
        ok = False

        for i in range(m_pts - 2):
            if ok:
                break
            x1, y1, _ = rpts[i]
            inv = [
                (
                    (x - x1) / ((x - x1) ** 2 + (y - y1) ** 2),
                    (y - y1) / ((x - x1) ** 2 + (y - y1) ** 2),
                    idx > i,
                )
                for x, y, idx in rpts
                if idx != i
            ]
            inv.sort()
            coords = [(x, y) for x, y, _ in inv]

            for j, (xj, yj, is_gt) in enumerate(inv):
                if not is_gt:
                    continue
                pos = [(ym - yj) / (xm - xj) for xm, ym in coords[j + 1 :]]
                if not pos:
                    continue
                neg = [(ym - yj) / (xm - xj) for xm, ym in coords[:j]]
                pos.sort()
                neg.sort()
                P = len(pos)
                L = len(neg)

                lo1 = k - L if k > L else 0
                hi1 = P if P < k + 1 else k + 1
                for idx in range(lo1, hi1):
                    s = pos[idx]
                    if s * xj - yj > eps:
                        if idx > 0 and s - pos[idx - 1] <= eps:
                            continue
                        need = k - idx
                        if (need == 0 or neg[L - need] > s + eps) and (
                            need == L or neg[L - need - 1] <= s + eps
                        ):
                            ok = True
                            break
                if ok:
                    break

                lo2 = P - 1 - k if P - 1 > k else 0
                hi2 = P if P < P - k + L else P - k + L
                for idx in range(lo2, hi2):
                    s = pos[idx]
                    if s * xj - yj < -eps:
                        if idx < P - 1 and pos[idx + 1] - s <= eps:
                            continue
                        need = k - (P - 1 - idx)
                        if (need == 0 or neg[need - 1] < s - eps) and (
                            need == L or neg[need] >= s - eps
                        ):
                            ok = True
                            break

        print("YES" if ok else "NO")

solve()