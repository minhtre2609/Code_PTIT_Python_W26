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
    first = lines[0].split()
    n = int(first[0])
    k = int(first[1])
    content = "\n".join(lines[1:1 + n]).lower()
    words = re.findall(r'[a-z0-9]+', content)
    counts = Counter(words)
    filtered = [(w, c) for w, c in counts.items() if c >= k]
    sorted_words = sorted(filtered, key=lambda x: (-x[1], x[0]))
    out = [f"{w} {c}" for w, c in sorted_words]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()