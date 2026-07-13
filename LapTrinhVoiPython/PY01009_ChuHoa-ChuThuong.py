s = input()
hoa = 0
thuong = 0
for ch in s:
    if ch.isupper(): hoa += 1
    elif ch.islower():thuong += 1
if thuong >= hoa: print(s.lower())
else: print(s.upper())
