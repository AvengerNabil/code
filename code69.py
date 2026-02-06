t = int(input())
for _ in range(t):
    n = input().strip()
    length = len(n)
    n_int = int(n)

    if n_int % 7 == 0:
        print(n)
        continue

    best = None
    best_diff = 10  # large number

    # Check all numbers with same digit count
    start = 10 if length == 2 else 100
    end = 99 if length == 2 else 999

    for num in range(start, end + 1):
        if num % 7 == 0:
            s = str(num)
            diff = sum(1 for a, b in zip(s, n) if a != b)
            if diff < best_diff:
                best_diff = diff
                best = s
                if diff == 1:  # can't get better
                    break
    print(best)
#https://codeforces.com/problemset/problem/1633/A