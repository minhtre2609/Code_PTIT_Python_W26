def tongchuso(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

def check(n):
    s = str(n)
    for i in range(len(s) - 1):
        if abs(int(s[i + 1]) - int(s[i])) != 2: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n) and tongchuso(n) % 10 == 0: print("YES")
    else: print("NO")