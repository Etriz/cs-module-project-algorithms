"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    # Your code here
    arr = sorted(arr)
    # print(arr)
    i = 0
    while i < len(arr):
        try:
            if arr[i] == arr[i + 1]:
                i += 2
            else:
                return arr[i]
        except:
            return arr[i]


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
