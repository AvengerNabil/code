# B. Friends and Candies — Correct Python Solution

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    # If total candies cannot be equally divided
    if total % n != 0:
        print(-1)
        continue

    avg = total // n

    # Count friends who already have <= avg
    k = 0
    for x in a:
        if x > avg:
            k += 1

    print(k)
#https://codeforces.com/problemset/problem/1538/B