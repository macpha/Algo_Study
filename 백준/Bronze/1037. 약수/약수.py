import sys
from math import *
input = sys.stdin.readline

N = int(input())
factor = list(map(int, input().split()))

print(max(factor) * min(factor))
