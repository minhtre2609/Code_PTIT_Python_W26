import sys


def solve_case(n, k, pts):
    if k < 0 or k > n - 3:
        return False
    alpha = 0.000123456789
    rpts = [
        (x + alpha * y, y - alpha * x, idx) for idx, (x, y) in enumerate(pts)
    ]
    eps = 1e-9

    for i in range(n - 2):
        x1, y1, _ = rpts[i]
        inv = []
        for x, y, idx in rpts:
            if idx == i:
                continue
            dx = x - x1
            dy = y - y1
            r2 = dx * dx + dy * dy
            if r2 == 0:
                continue
            inv.append((dx / r2, dy / r2, idx > i))

        inv.sort()
        coords = [(x, y) for x, y, _ in inv]

        for j, (xj, yj, is_gt) in enumerate(inv):
            if not is_gt:
                continue
            pos = [
                (ym - yj) / (xm - xj) for xm, ym in coords[j + 1 :] if xm > xj
            ]
            if not pos:
                continue
            neg = [(ym - yj) / (xm - xj) for xm, ym in coords[:j] if xm < xj]
            pos.sort()
            neg.sort()
            P = len(pos)
            L = len(neg)

            for idx, s in enumerate(pos):
                l0 = s * xj - yj
                if -eps <= l0 <= eps:
                    continue
                if l0 > 0:
                    if idx > 0 and s - pos[idx - 1] <= eps:
                        continue
                    need = k - idx
                    if 0 <= need <= L:
                        if (need == 0 or neg[L - need] > s + eps) and (
                            need == L or neg[L - need - 1] <= s + eps
                        ):
                            return True
                else:
                    if idx < P - 1 and pos[idx + 1] - s <= eps:
                        continue
                    cnt_pos = P - 1 - idx
                    need = k - cnt_pos
                    if 0 <= need <= L:
                        if (need == 0 or neg[need - 1] < s - eps) and (
                            need == L or neg[need] >= s - eps
                        ):
                            return True
    return False


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    t = int(float(data[idx]))
    idx += 1
    out = []
    for _ in range(t):
        if idx + 1 >= len(data):
            break
        n = int(float(data[idx]))
        k = int(float(data[idx + 1]))
        idx += 2
        pts = []
        for _ in range(n):
            if idx + 1 >= len(data):
                break
            pts.append((float(data[idx]), float(data[idx + 1])))
            idx += 2
        if solve_case(len(pts), k, pts):
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))


if __name__ == "__main__":
    main()