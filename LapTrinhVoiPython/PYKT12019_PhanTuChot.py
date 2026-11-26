t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_left = [0] * n
    cur_max = -1
    for i in range(n):
        max_left[i] = cur_max
        if a[i] > cur_max:
            cur_max = a[i]
            
    min_right = [0] * n
    cur_min = 10**18
    for i in range(n - 1, -1, -1):
        min_right[i] = cur_min
        if a[i] < cur_min:
            cur_min = a[i]
            
    ans = 0
    for i in range(n):
        if a[i] >= max_left[i] and a[i] < min_right[i]:
            ans += 1
            
    print(ans)