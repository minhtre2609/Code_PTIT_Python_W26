n = int(input())
lens = [len(input().split()) for _ in range(n)]
res = []
i = 0
while i < n:
    if lens[i] == 7:
        res.append(2)
        i += 4
    else:
        res.append(1)
        while i < n and lens[i] != 7:
            i += 1
print(len(res))
for x in res:
    print(x)