a = set(input().lower().split())
b = set(input().lower().split())
hop = sorted(a | b)
giao = sorted(a & b)
print(*hop)
print(*giao)

