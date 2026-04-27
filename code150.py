t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    perm = []

    # 1. Numbers >= k → descending
    perm.extend(range(n, k - 1, -1))

    # 2. Numbers between m+1 and k-1
    if k - m - 1 > 0:
        perm.extend(range(m + 1, k))

    # 3. Numbers <= m → ascending
    perm.extend(range(1, m + 1))

    print(*perm)
#https://codeforces.com/problemset/problem/1992/C