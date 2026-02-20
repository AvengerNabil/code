t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    prefix = [0] * n
    suffix = [0] * n

    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix[i] = len(seen)

    seen = set()
    for i in range(n - 1, -1, -1):
        seen.add(s[i])
        suffix[i] = len(seen)

    max_sum = 0
    for i in range(1, n):
        max_sum = max(max_sum, prefix[i - 1] + suffix[i])

    print(max_sum)
#https://codeforces.com/problemset/problem/1791/D