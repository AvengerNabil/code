# A. Question Marks — Correct Python Solution

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    cnt = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    # Count fixed answers (ignore '?')
    for ch in s:
        if ch in cnt:
            cnt[ch] += 1

    # For each option, we can score at most n
    ans = 0
    for ch in cnt:
        ans += min(cnt[ch], n)

    print(ans)
#https://codeforces.com/problemset/problem/1993/A