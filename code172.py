n = int(input())
bills = list(map(int, input().split()))

cnt25 = 0
cnt50 = 0

for b in bills:
    if b == 25:
        cnt25 += 1

    elif b == 50:
        if cnt25 == 0:
            print("NO")
            exit()
        cnt25 -= 1
        cnt50 += 1

    else:  # b == 100
        if cnt50 > 0 and cnt25 > 0:
            cnt50 -= 1
            cnt25 -= 1
        elif cnt25 >= 3:
            cnt25 -= 3
        else:
            print("NO")
            exit()

print("YES")
#https://codeforces.com/problemset/problem/349/A