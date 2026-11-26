import re

n = int(input())
a = []
for _ in range(n):
    s = input()
    nums = re.findall(r'\d+', s)
    for x in nums:
        a.append(int(x))

a.sort()
for x in a:
    print(x)