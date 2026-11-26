import sys

def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    it = iter(tokens)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        a.sort()
        ans = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            x = a[i]
            while l < r:
                val = x + a[l] + a[r]
                if val == 0:
                    ans += 1
                    l += 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
