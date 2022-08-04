import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = [0] * (N + 1)

sum_arr[1] = arr[0]
for _ in range(2, N + 1):
    sum_arr[_] = sum_arr[_ - 1] + arr[_ - 1]

result = []
for i in range(N - K + 1):
    result.append(sum_arr[i + K] - sum_arr[i])

print(max(result))
    
