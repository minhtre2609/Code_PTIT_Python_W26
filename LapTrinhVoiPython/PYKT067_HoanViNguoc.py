from itertools import permutations

t = int(input())
for _ in range(t):
    n = int(input())
    s = [str(i) for i in range(n, 0, -1)]
    res = ["".join(p) for p in permutations(s)]
    print(len(res))
    print(" ".join(res))