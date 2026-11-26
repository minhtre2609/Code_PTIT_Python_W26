import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    arr = [int(x) for x in raw[1:1 + n]]
    max_val = max(arr)
    ans = 0
    curr = 0
    for x in arr:
        if x == max_val:
            curr += 1
            if curr > ans:
                ans = curr
        else:
            curr = 0
    print(ans)

if __name__ == '__main__':
    solve()