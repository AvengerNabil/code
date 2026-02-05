def min_rest_days(n, a):
    # Initialize dp with infinity
    dp = [[float('inf')] * 3 for _ in range(n)]

    # Day 0 initialization
    if a[0] == 0:
        dp[0][0] = 1  # rest
    elif a[0] == 1:
        dp[0][1] = 0  # contest
        dp[0][0] = 1
    elif a[0] == 2:
        dp[0][2] = 0  # sport
        dp[0][0] = 1
    elif a[0] == 3:
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][0] = 1

    for i in range(1, n):
        # Always can rest
        dp[i][0] = min(dp[i - 1]) + 1

        # If contest possible today
        if a[i] == 1 or a[i] == 3:
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])

        # If sport possible today
        if a[i] == 2 or a[i] == 3:
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])

    return min(dp[n - 1])
#https://codeforces.com/problemset/problem/698/A