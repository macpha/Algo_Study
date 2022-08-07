import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

sum_price = 0
for i in range(N):
    a, b = map(int, input().split())
    sum_price += a * b

if sum_price == X:
    print("Yes")
else:
    print("No")
