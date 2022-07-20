import sys
input = sys.stdin.readline

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

N = int(input())
r = list(map(int, input().split()))

for i in range(1, N):
    print("%d/%d" %(r[0] // gcd(r[0], r[i]), r[i] // gcd(r[0], r[i])))
