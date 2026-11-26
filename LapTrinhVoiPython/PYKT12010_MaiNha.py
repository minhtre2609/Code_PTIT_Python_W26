import sys
from bisect import bisect_left, bisect_right, insort

def solve_one(n, A):
    L = []
    R = sorted(A[j] + j for j in range(n))
    ans = 10**18
    half = n // 2
    hi_bound = max(A) + n + 2
    for i in range(n):
        rv = A[i] + i
        R.pop(bisect_left(R, rv))
        insort(L, A[i] - i)
        h_min = i + 1 if i + 1 >= n - i else n - i
        lo = h_min
        hi = hi_bound
        while lo < hi:
            mid = (lo + hi) >> 1
            if bisect_right(L, mid - i) + bisect_right(R, mid + i) > half:
                hi = mid
            else:
                lo = mid + 1
        H = lo
        cost = 0
        tL = H - i
        for v in L:
            cost += tL - v if v < tL else v - tL
        tR = H + i
        for v in R:
            cost += tR - v if v < tR else v - tR
        if cost < ans:
            ans = cost
    return ans

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    L_data = len(data)
    out = []
    while idx < L_data:
        n = int(data[idx])
        A = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        out.append(str(solve_one(n, A)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()