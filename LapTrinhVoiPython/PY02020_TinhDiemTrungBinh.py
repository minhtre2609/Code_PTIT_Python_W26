n = int(input())
a = list(map(float, input().split()))
mn = min(a)
mx = max(a)
b = [x for x in a if x != mn and x != mx]
print(f"{sum(b) / len(b):.2f}")