import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    grid = []
    ptr = 2
    all_vals = []
    for _ in range(n):
        row = [int(x) for x in raw[ptr:ptr + m]]
        ptr += m
        grid.append(row)
        all_vals.extend(row)
    max_val = max(all_vals)
    min_val = min(all_vals)
    target = max_val - min_val
    positions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                positions.append((i, j))
    if not positions:
        print("NOT FOUND")
        return
    print(target)
    for r, c in positions:
        print(f"Vi tri [{r}][{c}]")

if __name__ == '__main__':
    solve()