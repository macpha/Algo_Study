import sys
input = sys.stdin.readline

def dfs(x):
    global result

    if x == N:
        result += 1
        
    else:
        for i in range(N):
            if not visited[i] and not left[i + x] and not right[N - 1 + x - i]:
                visited[i] = left[i + x] = right[N - 1 + x - i] = True
                dfs(x + 1)
                visited[i] = left[i + x] = right[N - 1 + x - i] = False

N = int(input())
visited = [False] * N
left = [False] * (2 * N - 1)
right = [False] * (2 * N - 1)
result = 0

dfs(0)

print(result)
