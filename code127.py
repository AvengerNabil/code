t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    last = {}
    ans = 0

    for i in range(n - 1, -1, -1):
        if s[i] in last:
            ans += last[s[i]] - i
        else:
            ans += n - i
        last[s[i]] = i

    print(ans)
#https://codeforces.com/problemset/problem/1917/B