import math

def krish(n):
    tong_giai_thua = sum(math.factorial(int(digit)) for digit in str(n))
    if (tong_giai_thua == n): return 'Yes'
    else: return 'No'

t = int(input())
for i in range(t):
    n = int(input())
    print(krish(n))