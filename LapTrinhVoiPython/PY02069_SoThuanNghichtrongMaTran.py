import sys

def is_pal(val):
    s = str(val)
    return len(s) >= 2 and s == s[::-1]

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    grid = []
    ptr = 2
    max_val = -1
    for i in range(n):
        row = [int(x) for x in raw[ptr:ptr + m]]
        ptr += m
        grid.append(row)
        for val in row:
            if val > max_val and is_pal(val):
                max_val = val
    if max_val == -1:
        print("NOT FOUND")
        return
    print(max_val)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == max_val:
                print(f"Vi tri [{i}][{j}]")

if __name__ == '__main__':
    solve()