import sys

def solve():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    students = []
    idx = 1
    for _ in range(n):
        name = lines[idx]
        c, t = map(int, lines[idx + 1].split())
        students.append((name, c, t))
        idx += 2
    students.sort(key=lambda s: (-s[1], s[2], s[0]))
    for name, c, t in students:
        print(f"{name} {c} {t}")

if __name__ == '__main__':
    solve()