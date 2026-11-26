f = open("CONTACT.in", "r")
s = set()
for line in f:
    email = line.strip().lower()
    if email:
        s.add(email)
f.close()

for email in sorted(s):
    print(email)