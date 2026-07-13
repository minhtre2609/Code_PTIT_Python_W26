t = int(input())
for _ in range(t):
    n = input().strip()
    digits = [int(j) for j in n]
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] >= 5:
            digits[i - 1] += 1
        digits[i] = 0
    if digits[0] == 10:
        print("10" + "".join(str(x) for x in digits[1:]))
    else:
        print("".join(str(x) for x in digits))