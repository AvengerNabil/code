from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    freq = defaultdict(int)
    freq[0] = 1  # prefix sum = 0 initially

    prefix = 0
    ans = 0

    for ch in s:
        prefix += int(ch) - 1
        ans += freq[prefix]
        freq[prefix] += 1

    print(ans)
#https://codeforces.com/problemset/problem/1398/C