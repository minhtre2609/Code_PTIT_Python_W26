import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    grid = []
    ptr = 2
    max_prime = -1
    for i in range(n):
        row = [int(x) for x in raw[ptr:ptr + m]]
        ptr += m
        grid.append(row)
        for val in row:
            if val > max_prime and is_prime(val):
                max_prime = val
    if max_prime == -1:
        print("NOT FOUND")
        return
    print(max_prime)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == max_prime:
                print(f"Vi tri [{i}][{j}]")

if __name__ == '__main__':
    solve()