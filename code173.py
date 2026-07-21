t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    dp = [-1] * n
    dp[0] = 0  # start at first cell (always '.')

    for i in range(1, n):
        if s[i] == '*':
            continue

        best = -1
        if i - 1 >= 0 and dp[i - 1] != -1:
            best = dp[i - 1]
        if i - 2 >= 0 and dp[i - 2] != -1:
            best = max(best, dp[i - 2])

        if best != -1:
            dp[i] = best + (1 if s[i] == '@' else 0)

    print(max(dp))
#https://codeforces.com/problemset/problem/1932/A