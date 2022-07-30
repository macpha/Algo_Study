import sys
input = sys.stdin.readline

n = int(input())

score = []
for _ in range(n):
    score.append(int(input()))

step = [0] * n
step[0] = score[0]
if n > 1:
    step[1] = step[0] + score[1]
if n > 2:
    step[2] = max(score[2] + step[0], score[2] + score[1])

for i in range(3, n):
    step[i] = max(score[i] + step[i - 2], score[i] + step[i - 3] + score[i - 1])
    
print(step[n - 1])
