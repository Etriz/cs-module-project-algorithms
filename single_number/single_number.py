"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    # Your code here
    # sort the array
    # arr = sorted(arr)
    # i = 0
    # while i < len(arr):
    #     try:
    #         # see if the value is the same as the next
    #         if arr[i] == arr[i + 1]:
    #             i += 2
    #         else:
    #             # if the value isnt the same as next return the value
    #             return arr[i]
    #     except:
    #         # if we get to the end and haven't found it return the last value
    #         return arr[i]

    for elem in arr:
        if arr.count(elem) == 1:
            return elem


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
