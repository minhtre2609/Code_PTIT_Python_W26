import sys

def mat_mul(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            a = Ai[k]
            if a:
                Bk = B[k]
                for j in range(n):
                    Ci[j] = (Ci[j] + a * Bk[j]) % 10
    return C

def mat_add(A, B, n):
    return [[(A[i][j] + B[i][j]) % 10 for j in range(n)] for i in range(n)]

def calc(A, k, n):
    if k == 1:
        return A, A
    P, S = calc(A, k >> 1, n)
    I_plus_P = [[(P[i][j] + (1 if i == j else 0)) % 10 for j in range(n)] for i in range(n)]
    S2 = mat_mul(S, I_plus_P, n)
    P2 = mat_mul(P, P, n)
    if k & 1:
        P2 = mat_mul(P2, A, n)
        S2 = mat_add(S2, P2, n)
    return P2, S2

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    idx = 2
    A = []
    for _ in range(n):
        A.append([int(x) % 10 for x in data[idx:idx + n]])
        idx += n
    _, S = calc(A, k, n)
    out = [" ".join(str(x) for x in row) for row in S]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()