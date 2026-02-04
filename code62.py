n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        mini = abs(x[i+1] - x[i])
        maxi = abs(x[-1] - x[i])
    elif i == n-1:
        mini = abs(x[i] - x[i-1])
        maxi = abs(x[i] - x[0])
    else:
        mini = min(abs(x[i] - x[i-1]), abs(x[i+1] - x[i]))
        maxi = max(abs(x[i] - x[0]), abs(x[i] - x[-1]))
    print(mini, maxi)
#https://codeforces.com/problemset/problem/567/A