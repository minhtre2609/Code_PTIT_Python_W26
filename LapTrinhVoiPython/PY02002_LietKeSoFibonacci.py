c = [0] * 93
c[0] = 0
c[1] = 1
c[2] = 1
for i in range(3, 93):
    c[i] = c[i-1] + c[i-2]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        print(c[j], end = " ")
    print()