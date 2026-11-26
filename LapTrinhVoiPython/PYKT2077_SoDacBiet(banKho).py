import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137}
    digits = [int(c) for c in str(N)][::-1]
    dp = {(0, 0, 0): 1}
    for d in digits:
        ndp = {}
        for (c, sx, sy), ways in dp.items():
            for dy in range(10):
                rem = d - c - 2 * dy
                dx = rem % 10
                nc = (dx + 2 * dy + c) // 10
                key = (nc, sx + dx, sy + dy)
                ndp[key] = ndp.get(key, 0) + ways
        dp = ndp
    ans = 0
    for (c, sx, sy), ways in dp.items():
        if c == 0 and sx in primes and sy in primes:
            ans += ways
    sys.stdout.write(str(ans) + "\n")

if __name__ == '__main__':
    solve()