t = int(input())
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    max_fibo = 0
    for a3 in [a1 + a2, a4 - a2, a5 - a4]:
        a = [a1, a2, a3, a4, a5]
        count = 0
        for i in range(3):
            if a[i + 2] == a[i] + a[i + 1]:
                count += 1
        max_fibo = max(max_fibo, count)
    print(max_fibo)
#https://codeforces.com/problemset/problem/2060/A