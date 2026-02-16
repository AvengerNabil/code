import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n == 2:
        print(-1)
        continue

    nums = []
    for x in range(1, n * n + 1, 2):
        nums.append(x)
    for x in range(2, n * n + 1, 2):
        nums.append(x)

    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(nums[idx])
            idx += 1
        print(*row)
#https://codeforces.com/problemset/problem/1520/C