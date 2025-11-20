t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    unique_count = len(set(a))
    max_len = min(unique_count, n - unique_count + 1)
    print(max_len)
#https://codeforces.com/problemset/problem/1692/B