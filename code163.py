# B. Food Buying — Correct Python Solution

t = int(input())
for _ in range(t):
    s = int(input())
    spent = 0
    while s > 0:
        x = s - (s % 10)
        if x == 0:
            spent += s
            break
        spent += x
        s = s - x + x // 10
    print(spent)
#https://codeforces.com/problemset/problem/1296/B