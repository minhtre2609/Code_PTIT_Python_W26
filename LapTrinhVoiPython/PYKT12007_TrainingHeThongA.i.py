t = int(input())
for _ in range(t):
    n = int(input())
    u = float(input())
    p = sorted(list(map(float, input().split())))
    
    p.append(1.0)
    for i in range(n):
        diff = p[i + 1] - p[i]
        cost = (i + 1) * diff
        if u >= cost:
            u -= cost
            for j in range(i + 1):
                p[j] = p[i + 1]
        else:
            add = u / (i + 1)
            for j in range(i + 1):
                p[j] += add
            u = 0
            break
            
    ans = 1.0
    for i in range(n):
        ans *= min(1.0, p[i])
        
    print(f"{ans:.6f}")