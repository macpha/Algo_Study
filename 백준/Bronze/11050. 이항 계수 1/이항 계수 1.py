import sys
input = sys.stdin.readline

N, K = map(int, input().split())

f = [i for i in range(N + 1)]
f[0] = 1

for i in range(2, N + 1):
    f[i] = f[i] * f[i - 1]

print(f[N] // (f[N - K] * f[K]))
