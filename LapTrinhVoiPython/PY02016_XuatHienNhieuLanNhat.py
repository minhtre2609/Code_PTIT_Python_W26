from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    val, freq = c.most_common(1)[0]
    if freq > n // 2:
        print(val)
    else:
        print("NO")