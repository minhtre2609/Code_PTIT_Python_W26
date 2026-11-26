from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = {0: 0}
    for i in range(n):
        li = l[i]
        ci = c[i]
        for g, cost in list(dp.items()):
            ng = gcd(g, li)
            nc = cost + ci
            if ng not in dp or dp[ng] > nc:
                dp[ng] = nc
    print(dp.get(1, -1))