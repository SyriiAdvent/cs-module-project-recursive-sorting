# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: 
        mid = len(arr) // 2 
        Left = arr[:mid] 
        Right = arr[mid:]

        # Recursion
        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                arr[k] = Left[i] 
                i += 1
            else: 
                arr[k] = Right[j] 
                j += 1
            k += 1

        # Check if any element was left.
        while i < len(Left): 
            arr[k] = Left[i] 
            i += 1
            k += 1

        while j < len(Right): 
            arr[k] = Right[j] 
            j += 1
            k += 1
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1; 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return; 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; 
            index = start2; 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
              
            arr[start] = value; 
  
            # Update all the pointers 
            start += 1; 
            mid += 1; 
            start2 += 1; 


def merge_sort_in_place(arr, l, r):
    if (left < right): 
  
        # Same as (left + right) / 2, but avoids overflow 
        # for large left and right
        mid = left + (right - left) // 2; 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, left, mid); 
        merge_sort_in_place(arr, mid + 1, right); 
  
        merge_in_place(arr, left, mid, right); 

