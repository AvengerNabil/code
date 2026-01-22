t = int(input())
for _ in range(t):
    s = input().strip()
    c = input().strip()
    n = len(s)
    ans = "NO"
    for i in range(n):
        if s[i] == c and i % 2 == 0 and (n - i - 1) % 2 == 0:
            ans = "YES"
            break
    print(ans)
#https://codeforces.com/problemset/problem/1650/A