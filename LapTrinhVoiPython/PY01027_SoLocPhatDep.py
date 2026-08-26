s = input()
i = 0
n = len(s)
while i < n:
    if i + 2 < n and s[i:i + 3] == "688": i += 3
    elif i + 1 < n and s[i:i + 2] == "68": i += 2
    elif s[i] == "6": i += 1
    else:
        print("NO")
        break
else:
    print("YES")