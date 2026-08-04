import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    prefix = 0
    seen = set()
    seen.add(0)

    found = False

    for i in range(n):
        if (i % 2) == 0:  # 0-based index → position i+1 is odd
            prefix += arr[i]
        else:
            prefix -= arr[i]

        if prefix in seen:
            found = True
            break

        seen.add(prefix)

    print("YES" if found else "NO")
#https://codeforces.com/problemset/problem/1915/E