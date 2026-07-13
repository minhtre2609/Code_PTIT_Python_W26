t = int(input())
for i in range(t):
    n = input()
    tich = 1
    for c in n:
        if c != '0': tich *= int(c)
    print(tich)
