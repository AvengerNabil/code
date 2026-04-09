a = input().strip()
b = input().strip()

if a == b:
    print(-1)
else:
    print(max(len(a), len(b)))
#https://codeforces.com/problemset/problem/766/A