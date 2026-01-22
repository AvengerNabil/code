t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()
    s2 = s + s  # duplicate for circular traversal

    # Precompute nearest 'g' after each index
    next_g = [-1] * (2 * n)
    last = -1
    for i in range(2 * n - 1, -1, -1):
        if s2[i] == 'g':
            last = i
        next_g[i] = last

    ans = 0
    for i in range(n):
        if s[i] == c:
            wait = next_g[i] - i
            ans = max(ans, wait)

    print(ans)
#https://codeforces.com/problemset/problem/1744/C