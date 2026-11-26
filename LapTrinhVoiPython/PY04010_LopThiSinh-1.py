class ThiSinh:
    def __init__(self, name, dob, d1, d2, d3):
        self.name = name
        self.dob = dob
        self.total = d1 + d2 + d3

    def __str__(self):
        return f"{self.name} {self.dob} {self.total:.1f}"

name = input().strip()
dob = input().strip()
d1 = float(input())
d2 = float(input())
d3 = float(input())
print(ThiSinh(name, dob, d1, d2, d3))