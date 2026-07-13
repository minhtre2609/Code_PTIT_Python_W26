a, k, n = map(int, input().split())
r = a % k
if r == 0:
    b = k
else:
    b = k - r
ok = False
while a + b <= n:
    print(b, end=" ")
    ok = True
    b += k
if not ok:
    print(-1)