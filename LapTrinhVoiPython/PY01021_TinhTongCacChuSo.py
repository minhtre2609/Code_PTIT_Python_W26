t = int(input())
for i in range(t):
    s = input()
    chu = []
    tong = 0;
    for i in(s):
        if i.isdigit():
            tong += int(i)
        else:
            chu.append(i)
    chu.sort()
    print("".join(chu) + str(tong))
