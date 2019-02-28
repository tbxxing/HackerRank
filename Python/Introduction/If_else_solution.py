N = int(input())

if N % 2 == 1:      # If N is odd
    print("Weird")
elif N % 2 == 0:    # If N is even
    if 2 <= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
