n = int(input())
teams = {}
for i in range(1, n + 1):
    m_team = f"Team{i:02d}"
    t_name = input().strip()
    u_name = input().strip()
    teams[m_team] = (t_name, u_name)

m = int(input())
ts = []
for i in range(1, m + 1):
    m_ts = f"C{i:03d}"
    name = input().strip()
    m_team = input().strip()
    t_name, u_name = teams[m_team]
    ts.append((m_ts, name, t_name, u_name))

ts.sort(key=lambda x: x[1])

for x in ts:
    print(f"{x[0]} {x[1]} {x[2]} {x[3]}")