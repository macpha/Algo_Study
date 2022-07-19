import sys
from math import *
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    count = 0
    n = int(input())
    for _ in range(n):
        x, y, r = map(int, input().split())

        if ((x - x1) ** 2) + ((y - y1) ** 2) > r * r:
            if ((x - x2) ** 2) + ((y - y2) ** 2) < r * r:
                count += 1

        if ((x - x1) ** 2) + ((y - y1) ** 2) < r * r:
            if ((x - x2) ** 2) + ((y - y2) ** 2) > r * r:
                count += 1

    print(count)
