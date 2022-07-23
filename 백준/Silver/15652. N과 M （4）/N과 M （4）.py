import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

def dfs(n):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(n, N + 1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)
