import sys

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(hull):
    n = len(hull)
    if n < 3:
        return 0.0
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]
    return abs(area) / 2.0

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
        ptr += 1
        points = []
        for _ in range(n):
            points.append((int(raw[ptr]), int(raw[ptr + 1])))
            ptr += 2
        hull = convex_hull(points)
        area = polygon_area(hull)
        out.append(f"{area:.3f}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()