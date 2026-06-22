# A. Verify Password — Correct Python Solution

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ok = True
    last_letter = ""
    last_digit = ""
    seen_letter = False

    for ch in s:
        if ch.isdigit():
            # digit after letter is not allowed
            if seen_letter:
                ok = False
                break
            if last_digit and ch < last_digit:
                ok = False
                break
            last_digit = ch
        else:  # letter
            seen_letter = True
            if last_letter and ch < last_letter:
                ok = False
                break
            last_letter = ch

    print("YES" if ok else "NO")
#https://codeforces.com/problemset/problem/1976/A