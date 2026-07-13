import math

t = int(input())
for i in range(t):
    n, x, m = map(float, input().split())
    nam = 0
    while (n < m):
        n = n + n * x / 100.0
        nam += 1
    print(nam)