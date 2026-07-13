n = int(input())
a = [0] * n
cnt = 0
for i in map(int, input().split()):
    if cnt > 0 and (a[cnt - 1] + i) % 2 == 0: cnt -= 1
    else:
        a[cnt] = i
        cnt += 1
print(cnt)

