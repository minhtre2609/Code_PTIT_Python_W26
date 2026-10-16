def thaphanoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    thaphanoi(n - 1, a, c, b)
    print(a, "->", c)
    thaphanoi(n - 1, b, a, c)


n = int(input())
thaphanoi(n, "A", "B", "C")