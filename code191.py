import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, b, s = map(int, input().split())

    min_sum = b * k
    max_sum = b * k + (k - 1) * n

    if s < min_sum or s > max_sum:
        print(-1)
        continue

    arr = [0] * n
    arr[0] = min_sum
    remaining = s - min_sum

    for i in range(n):
        add = min(remaining, k - 1)
        arr[i] += add
        remaining -= add

    print(*arr)
    #https://codeforces.com/problemset/problem/1715/B