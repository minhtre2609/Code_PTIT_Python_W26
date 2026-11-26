import sys

def get_partitions(rem, max_val):
    if rem == 0:
        return [[]]
    res = []
    for val in range(min(rem, max_val), 0, -1):
        for sub in get_partitions(rem - val, val):
            res.append([val] + sub)
    return res

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    t = int(raw[0])
    out = []
    for i in range(1, 1 + t):
        n = int(raw[i])
        parts = get_partitions(n, n)
        out.append(str(len(parts)))
        out.append(" ".join(f"({' '.join(map(str, p))})" for p in parts))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()