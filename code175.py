t = int(input())

for _ in range(t):
    n = int(input())
    answers = []

    power = 10
    while power <= 10**18:
        d = power + 1
        if n % d == 0:
            x = n // d
            answers.append(x)
        power *= 10

    if not answers:
        print(0)
    else:
        answers.sort()
        print(len(answers))
        print(*answers)
#https://codeforces.com/problemset/problem/2132/B