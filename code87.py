t = int(input())
for _ in range(t):
    a, b = input().split()

    if a == b:
        print("=")
        continue

    # If last character differs (S, M, L)
    if a[-1] != b[-1]:
        if a[-1] == 'S':
            print("<")
        elif a[-1] == 'L':
            print(">")
        elif b[-1] == 'S':
            print(">")
        else:
            print("<")
    else:
        # both end with 'S' or both end with 'L'
        if a[-1] == 'S':
            # More X's → smaller
            if len(a) > len(b):
                print("<")
            else:
                print(">")
        elif a[-1] == 'L':
            # More X's → larger
            if len(a) > len(b):
                print(">")
            else:
                print("<")
#https://codeforces.com/problemset/problem/1741/A