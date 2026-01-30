t = int(input())
for _ in range(t):
    s = input().strip()
    first = s.find('1')
    last = s.rfind('1')
    if first == -1:
        print(0)
    else:
        print(s[first:last+1].count('0'))
#https://codeforces.com/problemset/problem/1303/A