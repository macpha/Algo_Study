import sys
input = sys.stdin.readline

N = int(input())
result = []

for _ in range(N):
    result.append(list(map(int, input().split())))

for i in range(1, N):
    result[i][0] += min(result[i - 1][1], result[i - 1][2])
    result[i][1] += min(result[i - 1][0], result[i - 1][2])
    result[i][2] += min(result[i - 1][0], result[i - 1][1])

print(min(result[N - 1]))
