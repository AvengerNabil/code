from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    max_freq = max(freq.values())

    print(n - max_freq)
#https://codeforces.com/problemset/problem/2001/A