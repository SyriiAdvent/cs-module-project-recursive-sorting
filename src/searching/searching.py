# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid - 1)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # if arr[len(arr) - 1] > arr[0]:
    #     binary_search(arr, target, 0, len(arr) - 1)
    # else:
    #     binary_search(arr, target, len(arr) - 1, 0)
    pass