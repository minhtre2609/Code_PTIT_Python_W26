P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    try:
        line = input().strip()
        if not line:
            continue
        data = line.split()
        K = int(data[0])
        if K == 0:
            break
        S = data[1]
        res = ""
        for c in S:
            idx = P.index(c)
            new_idx = (idx + K) % 28
            res += P[new_idx]
        print(res[::-1])
    except:
        break