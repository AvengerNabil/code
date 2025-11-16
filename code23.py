t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # Condition: difference (n - m) must be even and m <= n
    if m <= n and (n - m) % 2 == 0:
        print("Yes")
    else:
        print("No")
#https://codeforces.com/problemset/problem/1977/A