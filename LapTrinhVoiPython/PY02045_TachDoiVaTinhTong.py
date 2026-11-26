import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    while len(s) > 1:
        mid = len(s) // 2
        a = int(s[:mid])
        b = int(s[mid:])
        s = str(a + b)
        sys.stdout.write(s + "\n")

solve()