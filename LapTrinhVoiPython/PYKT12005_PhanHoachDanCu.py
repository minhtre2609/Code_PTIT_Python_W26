t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    c1 = min(c, d)
    c2 = max(c, d)
    
    s1 = sum(a[:c1]) / c1
    s2 = sum(a[c1:c1+c2]) / c2
    
    print(f"{s1 + s2:.6f}")