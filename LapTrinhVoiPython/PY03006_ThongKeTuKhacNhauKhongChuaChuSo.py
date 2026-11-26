import sys
import re
from collections import Counter

def solve():
    data = sys.stdin.read()
    if not data:
        return
    lines = data.splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    content = "\n".join(lines[1:1 + n]).lower()
    words = re.findall(r'[a-z]+', content)
    counts = Counter(words)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    out = [f"{w} {c}" for w, c in sorted_words]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()