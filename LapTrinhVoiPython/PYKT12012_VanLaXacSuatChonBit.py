import sys

def sum_pop(n):
    if n <= 0:
        return 0
    ans = 0
    b = 0
    while (1 << b) <= n:
        p = 1 << (b + 1)
        h = 1 << b
        ans += ((n + 1) // p) * h + max(0, ((n + 1) % p) - h)
        b += 1
    return ans

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        la = a.bit_length()
        lb = b.bit_length()
        tot = 0.0
        for l in range(la, lb + 1):
            low = a if a > (1 << (l - 1)) else (1 << (l - 1))
            high = b if b < (1 << l) - 1 else (1 << l) - 1
            if low <= high:
                tot += (sum_pop(high) - sum_pop(low - 1)) / l
        out.append(f"{tot / (b - a + 1):.5f}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()