# A. Yes-Yes? — Correct Python Solution

t = int(input())
base = "Yes" * 100  # long enough to cover max |s| = 50

for _ in range(t):
    s = input().strip()
    print("YES" if s in base else "NO")
#https://codeforces.com/problemset/problem/1759/A