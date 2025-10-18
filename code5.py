t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    curr = x
    ops = 0
    found = False

    # Since length grows exponentially, max ops ~10 is enough for these constraints
    max_ops = 10

    while len(curr) < len(s) and ops <= max_ops:
        if s in curr:
            found = True
            break
        curr = curr + curr
        ops += 1

    # Final check in case length >= s length but s not found yet
    if not found and s in curr:
        found = True

    print(ops if found else -1)
#https://codeforces.com/problemset/problem/1881/A