while True:
    n = int(input())
    if n == 0:
        break
    a = [int(input()) for _ in range(n)]
    mn = min(a)
    mx = max(a)
    if mn == mx:
        print("BANG NHAU")
    else:
        print(mn, mx)