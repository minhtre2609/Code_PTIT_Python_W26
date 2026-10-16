t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    if n < 3:
        print("NO")
        continue

    ok = False

    for i in range(1, n - 1):
        check = True

        for j in range(1, i + 1):
            if s[j] <= s[j - 1]:
                check = False
                break

        if check:
            for j in range(i + 1, n):
                if s[j] >= s[j - 1]:
                    check = False
                    break

        if check:
            ok = True
            break

    print("YES" if ok else "NO")