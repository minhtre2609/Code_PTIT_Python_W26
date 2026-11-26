import sys

toks = list(map(int, sys.stdin.read().split()))
if toks:
    m = toks[0]
    n = toks[1]
    a = [toks[2 + i * n : 2 + (i + 1) * n] for i in range(m)]
    q = [(i, j) for i in range(m) for j in range(n) if a[i][j] == -1]
    ans = 0
    for i, j in q:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and a[ni][nj] != 0:
                    ans += a[ni][nj]
                    a[ni][nj] = 0
    print(ans)