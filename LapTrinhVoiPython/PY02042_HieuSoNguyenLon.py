import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    a = int(lines[0])
    b = int(lines[1])
    sys.stdout.write(str(a - b) + "\n")

solve()