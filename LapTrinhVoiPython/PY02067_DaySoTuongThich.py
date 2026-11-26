import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    arr = [int(x) for x in raw[1:1 + n]]
    min_val = min(arr)
    best_sum = 10**18
    for k in range(min_val, 0, -1):
        total = 0
        possible = True
        for x in arr:
            b = x // (k + 1) + 1
            if x // b != k:
                possible = False
                break
            total += b
        if possible and total < best_sum:
            best_sum = total
            break
    print(best_sum)

if __name__ == '__main__':
    solve()