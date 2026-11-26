n = int(input())
a = list(map(int, input().split()))
best_cost = None
best_val = None
for x in a:
    cost = sum(abs(y - x) for y in a)
    if best_cost is None or cost < best_cost:
        best_cost = cost
        best_val = x
print(best_cost, best_val)