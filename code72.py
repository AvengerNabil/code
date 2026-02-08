t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    pairs = set()
    for i in range(n - 1):
        pairs.add(s[i:i+2])
    print(len(pairs))
#https://codeforces.com/problemset/problem/1833/A