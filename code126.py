t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]

    ans = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            diff = 0
            for k in range(m):
                diff += abs(ord(words[i][k]) - ord(words[j][k]))
            ans = min(ans, diff)

    print(ans)
#https://codeforces.com/problemset/problem/1676/C