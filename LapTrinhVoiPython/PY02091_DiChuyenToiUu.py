import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    offsets = [(dx << 30) + dy for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy]
    for _ in range(t):
        xa = int(data[idx])
        ya = int(data[idx + 1])
        xb = int(data[idx + 2])
        yb = int(data[idx + 3])
        n = int(data[idx + 4])
        idx += 5
        allowed = set()
        for _ in range(n):
            x = int(data[idx])
            y1 = int(data[idx + 1])
            y2 = int(data[idx + 2])
            idx += 3
            base = x << 30
            for y in range(y1, y2 + 1):
                allowed.add(base | y)
        start = (xa << 30) | ya
        target = (xb << 30) | yb
        if start == target:
            out.append('0')
            continue
        allowed.discard(start)
        q = deque([(start, 0)])
        ans = -1
        while q:
            u, d = q.popleft()
            nd = d + 1
            found = False
            for off in offsets:
                v = u + off
                if v in allowed:
                    if v == target:
                        ans = nd
                        found = True
                        break
                    allowed.remove(v)
                    q.append((v, nd))
            if found:
                break
        out.append(str(ans))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()