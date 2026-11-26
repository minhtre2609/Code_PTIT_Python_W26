MOD = 1000

def mul(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def power(A, p):
    res = [[1, 0], [0, 1]]
    base = A
    while p > 0:
        if p % 2 == 1:
            res = mul(res, base)
        base = mul(base, base)
        p //= 2
    return res

t = int(input())
for c in range(1, t + 1):
    n = int(input())
    if n == 0:
        print(f"Case #{c}: 001")
        continue
    M = [[6, -4], [1, 0]]
    Pn = power(M, n - 1)
    
    an = (Pn[0][0] * 6 + Pn[0][1] * 2) % MOD
    ans = (an - 1 + MOD) % MOD
    print(f"Case #{c}: {ans:03d}")