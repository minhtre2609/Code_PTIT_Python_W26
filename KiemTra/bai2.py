t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    if all(x <= y for x, y in zip(a, b)):
        print("YES")
    else:
        print("NO")