import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        s = tokens[idx]
        n = tokens[idx + 1]
        idx += 2
        out.append(str(s.count(n)))
    sys.stdout.write("\n".join(out) + "\n")

solve()