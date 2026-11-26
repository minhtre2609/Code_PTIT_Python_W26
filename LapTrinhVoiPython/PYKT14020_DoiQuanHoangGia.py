import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        c = [int(x) for x in data[idx + 2:idx + 2 + n]]
        idx += 2 + n
        total = sum(c)
        high = total // k
        if high == 0:
            out.append('0')
            continue
        low = total // (k + n)
        ans = low
        if low < 1:
            low = 1
        while low <= high:
            mid = (low + high) // 2
            rows = 0
            rem = 0
            for x in c:
                tot = rem + x
                if tot >= mid:
                    rows += tot // mid
                    rem = tot % mid
                else:
                    rem = x
            if rows >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(ans * k))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()