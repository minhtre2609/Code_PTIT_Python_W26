import sys

def solve():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return
    n, m = map(int, lines[0].split())
    subjects = {}
    idx = 1
    for _ in range(n):
        code = lines[idx]
        name = lines[idx + 1]
        subjects[code] = name
        idx += 2
    exams = []
    for i in range(1, m + 1):
        parts = lines[idx].split()
        idx += 1
        code, d_str, t_str, group = parts[0], parts[1], parts[2], parts[3]
        dd, mm, yyyy = map(int, d_str.split('/'))
        hh, mins = map(int, t_str.split(':'))
        exam_id = f"T{i:03d}"
        exams.append(((yyyy, mm, dd, hh, mins, code, exam_id), f"{exam_id} {code} {subjects[code]} {d_str} {t_str} {group}"))
    exams.sort(key=lambda x: x[0])
    sys.stdout.write('\n'.join(x[1] for x in exams) + '\n')

if __name__ == '__main__':
    solve()