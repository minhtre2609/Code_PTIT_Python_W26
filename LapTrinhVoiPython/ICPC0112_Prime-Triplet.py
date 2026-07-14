import math

def nguyen_to(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0;
    for i in range(1, n + 1):
        if (i + 6 <= n):
            if ((nguyen_to(i) and nguyen_to(i + 2) and nguyen_to(i + 6)) or \
               (nguyen_to(i) and nguyen_to(i + 4) and nguyen_to(i + 6))):
                cnt += 1
    print(cnt)