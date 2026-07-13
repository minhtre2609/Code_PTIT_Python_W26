t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    if n == 0:
        print(0)
        continue
    res = ""
    while n > 0:
        r = n % b
        if r < 10:
            res += str(r)
        else:
            res += chr(ord('A') + r - 10)
        n //= b
    print(res[::-1])