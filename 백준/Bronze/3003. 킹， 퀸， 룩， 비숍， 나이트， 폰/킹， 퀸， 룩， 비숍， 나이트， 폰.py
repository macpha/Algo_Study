import sys
input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]

search = list(map(int, input().split()))

for i in range(len(search)):
    print(chess[i] - search[i], end = ' ')
    