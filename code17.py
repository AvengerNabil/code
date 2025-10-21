t = int (input ())
for _ in range (t):
    n = int (input ())
    a = list (map (int, input ().split ()))

    if all (x == a[0] for x in a):
        print ("NO")
    else:
        a.sort (reverse=True)
        prefix = 0
        ugly = False
        for i in range (n):
            if a[i] == prefix:
                # Try swapping with next if possible
                if i + 1 < n:
                    a[i], a[i + 1] = a[i + 1], a[i]
                else:
                    ugly = True
                    break
            prefix += a[i]
        if ugly:
            print ("NO")
        else:
            print ("YES")
            print (*a)
#https://codeforces.com/problemset/problem/1783/A