import sys
from math import *
input = sys.stdin.readline

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    big_r = max(r1, r2)
    small_r = min(r1, r2)

    if d > big_r:
        if d > r1 + r2:
            print("0")
        elif d == r1 + r2:
            print("1")
        else:
            print("2")
    else:
        if d + small_r < big_r:
            print("0")
        elif d + small_r == big_r:
            if d == 0:
                print("-1")
            else:
                print("1")
        else:
            print("2")
