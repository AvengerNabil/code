t = int (input ())
for _ in range (t):
    n = int (input ())
    a = list (map (int, input ().split ()))

    even = sum (1 for x in a if x % 2 == 0)
    odd = n - even

    if even % 2 == 0 and odd % 2 == 0:
        print ("YES")
    else:
        a.sort ()
        ok = False
        for i in range (n - 1):
            if abs (a[i] - a[i + 1]) == 1:
                ok = True
                break
        print ("YES" if ok else "NO")
#https://codeforces.com/problemset/problem/1360/C