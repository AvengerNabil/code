t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    i = 0
    deletions = 0
    while i < n:
        if s[i:i+3] == "pie" or s[i:i+3] == "map":
            deletions += 1
            i += 3  # skip past this "ugly" substring
        else:
            i += 1
    print(deletions)
#https://codeforces.com/problemset/problem/1941/C