import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    n = int(lines[0])
    grid = lines[1:1 + n]
    ans = 0
    for r in range(n):
        c = grid[r].count('C')
        ans += c * (c - 1) // 2
    for col in range(n):
        c = sum(1 for r in range(n) if grid[r][col] == 'C')
        ans += c * (c - 1) // 2
    print(ans)

solve()