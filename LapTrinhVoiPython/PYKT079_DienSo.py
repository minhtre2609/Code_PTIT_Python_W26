t = int(input())
for _ in range(t):
    n = int(input())
    s = set(map(int, input().split()))
    print(max(s) - min(s) + 1 - len(s))