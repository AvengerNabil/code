t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    xor_sum = 0
    for num in a:
        xor_sum ^= num

    if n % 2 == 1:
        print(xor_sum)
    else:
        if xor_sum == 0:
            print(0)
        else:
            print(-1)
#https://codeforces.com/problemset/problem/1805/A