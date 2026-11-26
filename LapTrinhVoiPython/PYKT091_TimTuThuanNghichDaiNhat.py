f = open("VANBAN.in", "r")
words = f.read().split()
f.close()

d = {}
max_len = 0
for w in words:
    if w == w[::-1]:
        if len(w) > max_len:
            max_len = len(w)
        d[w] = d.get(w, 0) + 1

for w in d:
    if len(w) == max_len:
        print(w, d[w])