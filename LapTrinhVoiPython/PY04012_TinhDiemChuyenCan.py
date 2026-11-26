import sys

def solve():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    students = []
    idx = 1
    for _ in range(n):
        s_id = lines[idx]
        name = lines[idx + 1]
        cls = lines[idx + 2]
        students.append((s_id, name, cls))
        idx += 3
    attendance = {}
    for _ in range(n):
        parts = lines[idx].split()
        attendance[parts[0]] = parts[1]
        idx += 1
    for s_id, name, cls in students:
        att = attendance[s_id]
        score = max(0, 10 - att.count('m') - 2 * att.count('v'))
        extra = " KDDK" if score == 0 else ""
        print(f"{s_id} {name} {cls} {score}{extra}")

if __name__ == '__main__':
    solve()