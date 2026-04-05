t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())


    # distance clockwise function
    def dist(x, start):
        return (x - start) % 12


    red_dist = dist(b, a)
    c_dist = dist(c, a)
    d_dist = dist(d, a)

    # Check if c and d are on opposite sides of red string
    if (0 < c_dist < red_dist and (d_dist > red_dist or d_dist == 0)) or \
            (0 < d_dist < red_dist and (c_dist > red_dist or c_dist == 0)):
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/1971/C