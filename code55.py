t = int(input())
for _ in range(t):
    n = input().strip()
    if int(n) % 7 == 0:
        print(n)
        continue
    found = False
    for i in range(len(n)):
        for d in '0123456789':
            if i == 0 and d == '0':
                continue
            if d == n[i]:
                continue
            new_n = n[:i] + d + n[i+1:]
            if int(new_n) % 7 == 0:
                print(new_n)
                found = True
                break
        if found:
            break
#https://codeforces.com/problemset/problem/1633/A