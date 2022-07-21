import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        value, key = input().split()
        if key not in clothes:
            clothes[key] = list()
        clothes[key].append(value)

    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1

    print(count - 1)
