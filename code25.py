from collections import Counter

t = int (input ())
for _ in range (t):
    n = int (input ())
    a = list (map (int, input ().split ()))
    freq = Counter (a)

    distinct = len (freq)  # how many unique skills
    most_common = max (freq.values ())  # max frequency of any skill

    # Answer is min(max(distinct - 1, most_common), min(distinct, most_common))
    # Simplified known formula:
    ans = min (most_common, distinct - 1)
    ans = max (ans, min (most_common - 1, distinct))

    print (ans)
#https://codeforces.com/problemset/problem/1335/C