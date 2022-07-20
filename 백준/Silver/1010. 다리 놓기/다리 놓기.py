import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    f = [i for i in range(K + 1)]
    f[0] = 1

    for i in range(2, K + 1):
        f[i] = f[i] * f[i - 1]

    print(f[K] // (f[K - N] * f[N]))
