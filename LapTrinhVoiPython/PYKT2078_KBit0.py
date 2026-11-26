from math import comb

def count_up_to(N, K):
    if N < 0:
        return 0
    if N == 0:
        return 1 if K == 1 else 0
    
    b = bin(N)[2:]
    L = len(b)
    
    total = 0
    if K == 1:
        total += 1
        
    for l in range(1, L):
        zeros_needed = K
        ones_needed = (l - 1) - zeros_needed
        if ones_needed >= 0:
            total += comb(l - 1, zeros_needed)
            
    zeros_seen = 0
    for i in range(1, L):
        if b[i] == '1':
            rem_pos = L - 1 - i
            zeros_needed = K - (zeros_seen + 1)
            if 0 <= zeros_needed <= rem_pos:
                total += comb(rem_pos, zeros_needed)
        else:
            zeros_seen += 1
            
    if b.count('0') == K:
        total += 1
        
    return total

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_up_to(n, k))