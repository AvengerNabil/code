import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = [a[0]]

    for i in range(1, n):
        if a[i] != a[i - 1]:
            b.append(a[i])

    if len(b) == 1:
        print(1)
        continue

    ans = 2

    for i in range(1, len(b) - 1):
        if (b[i] > b[i - 1] and b[i] > b[i + 1]) or (b[i] < b[i - 1] and b[i] < b[i + 1]):
            ans += 1

    print(ans) #https://codeforces.com/problemset/problem/1832/C