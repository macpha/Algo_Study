import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

rest_arr = [0] * M
sum_arr = 0
for _ in range(N):
    sum_arr += arr[_]
    rest_arr[sum_arr % M] += 1

count = rest_arr[0]
for i in range(M):
    if rest_arr[i] == 0:
        continue

    count += rest_arr[i] * (rest_arr[i] - 1) // 2

print(count)
