import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    from collections import defaultdict

    runA = defaultdict(int)
    runB = defaultdict(int)

    # Compute longest runs in a
    count = 1
    for i in range(1, n + 1):
        if i < n and a[i] == a[i - 1]:
            count += 1
        else:
            runA[a[i - 1]] = max(runA[a[i - 1]], count)
            count = 1

    # Compute longest runs in b
    count = 1
    for i in range(1, n + 1):
        if i < n and b[i] == b[i - 1]:
            count += 1
        else:
            runB[b[i - 1]] = max(runB[b[i - 1]], count)
            count = 1

    answer = 0

    # Check all values
    for x in set(runA.keys()) | set(runB.keys()):
        answer = max(answer, runA[x] + runB[x])

    print(answer)
#https://codeforces.com/problemset/problem/1831/B