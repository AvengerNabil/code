from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()

    all_words = p1 + p2 + p3
    freq = Counter(all_words)

    s1 = s2 = s3 = 0

    for w in p1:
        if freq[w] == 1:
            s1 += 3
        elif freq[w] == 2:
            s1 += 1

    for w in p2:
        if freq[w] == 1:
            s2 += 3
        elif freq[w] == 2:
            s2 += 1

    for w in p3:
        if freq[w] == 1:
            s3 += 3
        elif freq[w] == 2:
            s3 += 1

    print(s1, s2, s3)
#https://codeforces.com/problemset/problem/1722/C