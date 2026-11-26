with open('DATA1.in', 'r') as f:
    s1 = set(f.read().lower().split())

with open('DATA2.in', 'r') as f:
    s2 = set(f.read().lower().split())

diff1 = sorted(list(s1 - s2))
diff2 = sorted(list(s2 - s1))

print(' '.join(diff1))
print(' '.join(diff2))