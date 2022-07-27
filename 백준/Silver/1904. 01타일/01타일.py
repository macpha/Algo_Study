import sys
input = sys.stdin.readline

N = int(input())
num = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    num[i] = num[i - 2] + num[i - 1] % 15746

print(num[N] % 15746)
