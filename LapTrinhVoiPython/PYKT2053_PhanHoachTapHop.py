import sys

def solve_one(n, A):
    tot = sum(A)
    if tot % 3 != 0:
        return 0
    target = tot // 3
    sums = [0] * (1 << n)
    for i in range(n):
        v = A[i]
        bit = 1 << i
        for m in range(bit):
            sums[m | bit] = sums[m] + v
    valid = [m for m in range(1, (1 << n) - 1) if sums[m] == target]
    valid_set = set(valid)
    full = (1 << n) - 1
    ans = 0
    for m1 in valid:
        rem = full ^ m1
        sub = rem
        while sub:
            if sub in valid_set and (rem ^ sub) in valid_set:
                ans += 1
            sub = (sub - 1) & rem
    return ans

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        A = [int(x) for x in data[idx + 1:idx + 1 + n]]
        idx += 1 + n
        out.append(str(solve_one(n, A)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()