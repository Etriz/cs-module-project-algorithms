"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Your code here
    window_start = 0
    max_values = []
    # while window doesnt go past end of array
    while window_start + k <= len(nums):
        # only look at nums in window
        range_max = nums[window_start]
        for index in range(window_start, window_start + k):
            #! find max num in window
            if nums[index] > range_max:
                range_max = nums[index]
        # print(range_max)
        max_values.append(range_max)
        # move window right 1 space
        window_start += 1

    return max_values


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    # should be 3,3,5,5,6,7
