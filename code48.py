t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    r = s % 3
    if r == 0:
        print(0)
    else:
        cnt = sum(1 for x in arr if x % 3 == r)
        if cnt > 0:
            print(1)
        else:
            print(2)
#https://codeforces.com/problemset/problem/1933/B