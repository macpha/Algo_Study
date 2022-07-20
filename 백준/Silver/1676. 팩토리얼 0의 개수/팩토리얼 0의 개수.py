import sys
input = sys.stdin.readline

N = int(input())

f = [i for i in range(N + 1)]
f[0] = 1

for i in range(2, N + 1):
    f[i] = f[i] * f[i - 1]

f_N = str(f[N])

count = 0
for digit in f_N[::-1]:
    if int(digit) == 0:
        count += 1
    else:
        break

print(count)
