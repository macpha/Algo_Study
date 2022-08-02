import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

result = [0] * n
result[0] = arr[0]
if n > 1:
    result[1] = result[0] + arr[1]
if n > 2:
    result[2] = max(arr[2] + result[0], arr[2] + arr[1], result[1])

for i in range(3, n):
    result[i] = max(arr[i] + result[i - 2], arr[i] + result[i - 3] + arr[i - 1], result[i - 1])

print(max(result))
