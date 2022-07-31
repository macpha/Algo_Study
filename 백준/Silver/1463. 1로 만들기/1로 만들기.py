import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * (N + 1)

for x in range(2, N + 1):
    arr[x] = arr[x - 1] + 1
    if x % 2 == 0:
        arr[x] = min(arr[x], arr[x // 2] + 1)
    if x % 3 == 0:
        arr[x] = min(arr[x], arr[x // 3] + 1)

print(arr[N])
