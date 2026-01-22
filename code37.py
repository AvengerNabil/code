t = int(input())
for _ in range(t):
    n = int(input())
    mins = []
    seconds = []
    for _ in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        mins.append(arr[0])
        seconds.append(arr[1])

    ans = sum(seconds) + min(mins)
    print(ans)
#https://codeforces.com/problemset/problem/1859/B