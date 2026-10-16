import math

t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for k in range(2, int(math.sqrt(2 * n)) + 1):
        x = n - k * (k - 1) // 2
        if x > 0 and x % k == 0:
            ans += 1
    print(ans)