t = int(input())

for _ in range(t):
    x, n, m = map(int, input().split())

    # Apply Void Absorption as much as possible
    while n > 0 and x > 20:  # VA is useful only if h > 20
        x = x // 2 + 10
        n -= 1

    # Apply Lightning Strikes
    x -= m * 10

    # Check if dragon defeated
    if x <= 0:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/1337/B