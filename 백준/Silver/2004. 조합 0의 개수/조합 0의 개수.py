import sys
input = sys.stdin.readline

def count2(N):
    count = 0
    while N >= 2:
        count += N // 2
        N //= 2

    return count

def count5(N):
    count = 0
    while N >= 5:
        count += N // 5
        N //= 5

    return count

n, m = map(int, input().split())

c2 = count2(n) - count2(n - m) - count2(m)
c5 = count5(n) - count5(n - m) - count5(m)

print(min(c2, c5))
