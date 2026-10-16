t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    mid = n // 2
    a = s[:mid]
    b = s[mid:]
    ra = sum(ord(c) - ord('A') for c in a) % 26
    rb = sum(ord(c) - ord('A') for c in b) % 26
    a = ''.join(chr((ord(c) - ord('A') + ra) % 26 + ord('A')) for c in a)
    b = ''.join(chr((ord(c) - ord('A') + rb) % 26 + ord('A')) for c in b)
    ans = ''
    for i in range(mid):
        x = ord(a[i]) - ord('A')
        y = ord(b[i]) - ord('A')
        ans += chr(((x + y) % 26) + ord('A'))
    print(ans)