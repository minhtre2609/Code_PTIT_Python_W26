t = int(input())
for _ in range(t):
    s = input().strip()
    if len(set(s)) != 2:
        print("NO")
    elif s[0::2] == s[0] * len(s[0::2]) and s[1::2] == s[1] * len(s[1::2]):
        print("YES")
    else:
        print("NO")