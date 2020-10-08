"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    #! Your code here
    # base cases
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )


"""
4           5
===         ===
1 1 1 1     11111
1 1 2       1112
1 2 1       1121
2 1 1       1211
1 3         2111
3 1         122
2 2         212
            221
            113
            131
            311
            32
            23
"""
