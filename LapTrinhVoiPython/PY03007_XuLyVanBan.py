import sys
import re

def solve():
    data = sys.stdin.read()
    if not data:
        return
    sentences = re.split(r'[.?!]', data)
    out = []
    for s in sentences:
        words = s.split()
        if words:
            clean = " ".join(w.lower() for w in words).capitalize()
            out.append(clean)
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()