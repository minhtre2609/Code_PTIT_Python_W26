import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    k = int(raw[1])
    if n == 0:
        print(0)
        return
    arr = [int(x) for x in raw[2:2 + n]]
    arr.sort()
    count = 1
    for i in range(1, n):
        if arr[i] - arr[i - 1] > k:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()