import sys
from itertools import combinations

a = [int(x) for x in sys.stdin.read().split()]
if len(a) == 12:
    all_indices = set(range(12))
    ans = float('inf')
    
    for c1 in combinations(range(1, 12), 2):
        g1 = (0,) + c1
        rem1 = all_indices - set(g1)
        s1 = sum(a[i] for i in g1)
        first_rem1 = min(rem1)
        choices2 = rem1 - {first_rem1}
        
        for c2 in combinations(choices2, 2):
            g2 = (first_rem1,) + c2
            rem2 = rem1 - set(g2)
            s2 = sum(a[i] for i in g2)
            first_rem2 = min(rem2)
            choices3 = rem2 - {first_rem2}
            
            for c3 in combinations(choices3, 2):
                g3 = (first_rem2,) + c3
                g4 = tuple(rem2 - set(g3))
                s3 = sum(a[i] for i in g3)
                s4 = sum(a[i] for i in g4)
                
                diff = max(s1, s2, s3, s4) - min(s1, s2, s3, s4)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        break
            if ans == 0:
                break
        if ans == 0:
            break
            
    print(ans)