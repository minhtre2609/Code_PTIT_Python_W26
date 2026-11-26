import sys

input = sys.stdin.read
data = input().split()
if data:
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]

    all_ors = set()
    cur_ors = set()

    for x in a:
        next_ors = {x}
        for v in cur_ors:
            next_ors.add(v | x)
        cur_ors = next_ors
        all_ors.update(cur_ors)

    print(len(all_ors))