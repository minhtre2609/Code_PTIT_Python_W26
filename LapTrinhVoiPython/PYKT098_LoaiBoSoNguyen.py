def is_int(s):
    try:
        val = int(s)
        return -2147483648 <= val <= 2147483647
    except:
        return False

f = open("DATA.in", "r")
words = f.read().split()
f.close()

res = []
for w in words:
    if not is_int(w):
        res.append(w)

res.sort()
print(" ".join(res))