import math
def so(n):
    if(n < 2):
        return False
    for i in range(2,math.isqrt(n)+1):
        if(n % i == 0):
            return False
    return True
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    ucln = math.gcd(a,b)
    tong = 0
    while(ucln > 0):
        tong += ucln % 10
        n = ucln // 10
    if so(tong):
        print("YES")
    else:
        print("NO")

a = [0 * n]
for i in range(len(n)):
