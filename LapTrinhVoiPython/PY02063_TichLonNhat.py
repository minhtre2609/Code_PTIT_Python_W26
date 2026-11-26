import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    arr = [int(x) for x in raw[1:1 + n]]
    arr.sort()
    ans = max(
        arr[-1] * arr[-2],
        arr[0] * arr[1],
        arr[-1] * arr[-2] * arr[-3],
        arr[0] * arr[1] * arr[-1]
    )
    print(ans)

if __name__ == '__main__':
    solve()