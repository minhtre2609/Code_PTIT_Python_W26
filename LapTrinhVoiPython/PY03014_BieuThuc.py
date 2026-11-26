import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        return
    t = int(lines[idx].strip())
    idx += 1
    out = []
    for _ in range(t):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        if idx >= len(lines):
            break
        s = lines[idx]
        idx += 1
        stack = []
        counter = 0
        res = []
        for ch in s:
            if ch == '(':
                counter += 1
                stack.append(counter)
                res.append(str(counter))
            elif ch == ')':
                top = stack.pop()
                res.append(str(top))
        out.append(" ".join(res))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()