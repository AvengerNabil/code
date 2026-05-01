# C. Ternary XOR — Correct Python Code (Accepted)

t = int(input())

for _ in range(t):
    n = int(input())
    x = input().strip()

    a = []
    b = []
    diff = False   # becomes True once a < b lexicographically is fixed

    for i in range(n):
        d = x[i]

        if d == '0':
            a.append('0')
            b.append('0')

        elif d == '1':
            if not diff:
                a.append('1')
                b.append('0')
                diff = True
            else:
                a.append('0')
                b.append('1')

        else:  # d == '2'
            if not diff:
                a.append('1')
                b.append('1')
            else:
                a.append('0')
                b.append('2')

    print("".join(a))
    print("".join(b))
#https://codeforces.com/problemset/problem/1328/C