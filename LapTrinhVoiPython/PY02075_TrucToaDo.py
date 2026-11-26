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
        ptr += 1
        intervals = []
        for _ in range(n):
            intervals.append((int(raw[ptr]), int(raw[ptr + 1])))
            ptr += 2
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        last_end = -1
        for start, end in intervals:
            if start >= last_end:
                cnt += 1
                last_end = end
        out.append(str(cnt))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()