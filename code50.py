t = int (input ())
for _ in range (t):
    n, m = map (int, input ().split ())
    carpet = [input ().strip () for _ in range (n)]

    target = "vika"
    idx = 0  # index in the target string

    for col in range (m):
        if any (carpet[row][col] == target[idx] for row in range (n)):
            idx += 1
            if idx == 4:
                break

    print ("YES" if idx == 4 else "NO")
#https://codeforces.com/problemset/problem/1862/A