a = []
while len(a) < 10:
    a.extend(map(int, input().split()))
s = set()
for x in a:
    s.add(x % 42)
print(len(s))