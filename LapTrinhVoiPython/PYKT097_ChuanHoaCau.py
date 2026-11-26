import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    words = line.strip().split()
    if not words:
        continue
    
    last = words[-1]
    if last in ['.', '!', '?']:
        words.pop()
        mark = last
    elif last[-1] in ['.', '!', '?']:
        mark = last[-1]
        words[-1] = last[:-1]
    else:
        mark = '.'
    
    cau = ' '.join(words).lower()
    if not cau:
        continue
    cau = cau[0].upper() + cau[1:] + mark
    print(cau)