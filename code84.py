def possible(x, y, z):
    for i in range(31):  # check each bit from 0 to 30
        xi = (x >> i) & 1
        yi = (y >> i) & 1
        zi = (z >> i) & 1

        # invalid combinations for this bit position
        if (xi == 0 and yi == 1 and zi == 1) or \
           (xi == 1 and yi == 0 and zi == 1) or \
           (xi == 1 and yi == 1 and zi == 0):
            return False
    return True


t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print("YES" if possible(x, y, z) else "NO")
#https://codeforces.com/problemset/problem/2153/B