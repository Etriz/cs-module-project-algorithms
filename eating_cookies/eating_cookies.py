"""
Input: an integer
Returns: an integer
"""

# from functools import lru_cache


# @lru_cache(maxsize=128)  # use built in lru cache instead of writing from scratch
def eating_cookies(n):
    #! Your code here
    # base cases
    # if n <= 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # else:
    #     return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

    #! better try - using memoization
    num_cache = {}
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        if n in num_cache:
            print(f"num {n} in cache ")
            return num_cache[n]
        else:
            #! still doesnt seem to be storing values in num_cache
            res = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
            num_cache[n] = res
            # print(f"{n} in cache")
            return num_cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 30

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
