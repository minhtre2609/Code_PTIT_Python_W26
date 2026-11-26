digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    res = ""
    while n > 0:
        res = digits[n % b] + res
        n //= b
    print(res)