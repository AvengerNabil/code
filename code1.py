t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    if B == 1:
        print("NO")
    else:
        print("YES")
        x = A
        y = A * B
        z = A * (B + 1)
        print(x, y, z)