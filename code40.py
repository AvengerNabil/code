t = int (input ())  # Number of test cases

for _ in range (t):
    n = int (input ())
    a = list (map (int, input ().split ()))

    abs_sum = sum (abs (x) for x in a)  # Sum of absolute values
    min_abs = min (abs (x) for x in a)  # Smallest absolute value

    negative_count = sum (1 for x in a if x < 0)  # Count negative numbers

    # If negative count is even, we can make all positive
    # If negative count is odd, subtract twice the smallest absolute value
    if negative_count % 2 == 0:
        print (abs_sum)
    else:
        print (abs_sum - 2 * min_abs)
#https://codeforces.com/problemset/problem/1791/E