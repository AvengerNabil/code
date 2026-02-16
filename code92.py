t = int(input())
for _ in range(t):
    n = int(input())

    if n % 2 == 1 or n < 4:
        print(-1)
        continue

    maxi = n // 4
    mini = (n + 5) // 6

    print(mini, maxi)
#https://codeforces.com/problemset/problem/1679/A