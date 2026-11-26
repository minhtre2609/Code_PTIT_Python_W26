t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (sum(int(c) for c in str(x)), x))
    print(*a)