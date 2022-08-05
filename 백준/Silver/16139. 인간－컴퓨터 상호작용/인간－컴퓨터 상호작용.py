import sys
input = sys.stdin.readline

S = input().rstrip()
S_a = list(set(S))
S_anum = []
a_num = [0] * len(S_a)

for a in S:
    a_num[S_a.index(a)] += 1
    S_anum.append(a_num[:])
    
q = int(input())
for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    if a in S_a:
        j = S_a.index(a)
        if l == 0:
            result = S_anum[r][j]
        else:
            result = S_anum[r][j] - S_anum[l - 1][j]
        print(result)
    else:
        print(0)
