import sys

def build_hull(lines):
    hull = []
    pts = []
    for m, c in lines:
        while hull:
            m1, c1 = hull[-1]
            if m1 == m:
                if c <= c1:
                    break
                hull.pop()
                if pts:
                    pts.pop()
                continue
            x = (c1 - c) / (m - m1)
            if not pts or x > pts[-1]:
                hull.append((m, c))
                pts.append(x)
                break
            hull.pop()
            pts.pop()
        else:
            hull.append((m, c))
    return hull, pts

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    p = [0.0] * (n + 1)
    s = 0.0
    for i in range(n):
        s += float(data[i + 1])
        p[i + 1] = s
    lines1 = [(float(i), p[i]) for i in range(n + 1)]
    lines2 = [(float(-i), -p[i]) for i in range(n - 1, -1, -1)]
    lines2.insert(0, (float(-n), -p[n]))
    h1, p1 = build_hull(lines1)
    h2, p2 = build_hull(lines2)
    i = 0
    j = 0
    l1 = len(p1)
    l2 = len(p2)
    ans = (h1[0][0] + h2[0][0]) * (-10000.0) + h1[0][1] + h2[0][1]
    while i < l1 or j < l2:
        if i < l1 and (j == l2 or p1[i] < p2[j]):
            x = p1[i]
            i += 1
        else:
            x = p2[j]
            j += 1
        val = (h1[i][0] + h2[j][0]) * x + h1[i][1] + h2[j][1]
        if val < ans:
            ans = val
    sys.stdout.write(f"{ans:.6f}\n")

if __name__ == '__main__':
    solve()