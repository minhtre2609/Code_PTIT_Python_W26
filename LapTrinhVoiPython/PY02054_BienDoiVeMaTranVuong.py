import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    grid = []
    ptr = 2
    for _ in range(n):
        grid.append([int(x) for x in raw[ptr:ptr + m]])
        ptr += m
    if n > m:
        remove_count = n - m
        removed_rows = {2 * i for i in range(remove_count)}
        kept_rows = [grid[r] for r in range(n) if r not in removed_rows]
        for row in kept_rows:
            print(*(row))
        return
    if m > n:
        remove_count = m - n
        removed_cols = {2 * i + 1 for i in range(remove_count)}
        for row in grid:
            kept_vals = [row[c] for c in range(m) if c not in removed_cols]
            print(*(kept_vals))
        return
    for row in grid:
        print(*(row))

if __name__ == '__main__':
    solve()