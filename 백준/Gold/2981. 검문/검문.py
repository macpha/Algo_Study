import sys
from math import *
input = sys.stdin.readline

def gcd(n, m):
    if m % n == 0:
        return n
    return gcd(m % n, n)

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))
num.sort()

g = num[1] - num[0]
for i in range(2, N):
    g = gcd(g, num[i] - num[i - 1])

result = []
for i in range(2, int(sqrt(g)) + 1):
    if g % i == 0:
        result.append(i)
        result.append(g // i)
result.append(g)

result = sorted(list(set(result)))
for r in result:
    print(r)
