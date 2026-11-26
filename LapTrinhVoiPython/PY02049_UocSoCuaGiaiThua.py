t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    cnt = 0
    while n >= p:
        cnt += n // p
        n //= p
    print(cnt)