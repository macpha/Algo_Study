import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

sum_arr = sum(arr[:K])
result = sum_arr

for i in range(N - K):
    sum_arr = sum_arr - arr[i] + arr[i + K]
    if result < sum_arr:
        result = sum_arr

print(result)