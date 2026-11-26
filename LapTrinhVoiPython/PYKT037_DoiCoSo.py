digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    res = []
    while n > 0:
        res.append(digits[n % b])
        n //= b
    print("".join(reversed(res)) if res else "0")