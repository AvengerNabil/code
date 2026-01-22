n = int(input())
a = list(map(int, input().split()))

a.sort()

can_form = False
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        can_form = True
        break

print("YES" if can_form else "NO")
#https://codeforces.com/problemset/problem/1744/C