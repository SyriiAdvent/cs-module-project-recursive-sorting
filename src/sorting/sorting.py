# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    sortedArray = [0] * (len(left) + len(right))
		
    # k is a pointer for the sortedArray current index position
    # i is a position pointer for the left half Array
    # j is a position pointer for the right half Array
    i = j = k = 0
    
    # while there still is numbers in the left and right array
    # i and j still point to a index position
    while i < len(left) and j < len(right):
        # if left[i] position is less then right[j]
        # add it to the sortedArray[k] position
        if left[i] <= right[j]:
            sortedArray[k] = left[i]
            i += 1 # then increment left[i] posiiton
        else:
            sortedArray[k] = right[j]
            j += 1
        # incrememnt k position since were 
        # done with that index position
        k += 1
    
    # if theres number remaining in left array
    # add them to the sortedArray
    while i < len(left):
        sortedArray[k] = left[i]
        # incrememnt after done adding numbers
        i += 1
        k += 1
        
    # if theres number remaining in right array
    # add them to the sortedArray
    while j < len(right):
        sortedArray[k] = right[j]
        # incrememnt after done adding numbers
        j += 1
        k += 1
        
    return sortedArray

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: 
        mid = len(arr) // 2 
        left = arr[:mid] 
        right = arr[mid:]

        # Recursion
        merge_sort(left)
        merge_sort(right)

        return merge(merge_sort(left), merge_sort(right))
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
    while start <= mid and start2 <= end: 
  
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


def merge_sort_in_place(arr, left, right):
    if (left < right): 
  
        # Same as (left + right) / 2, but avoids overflow 
        # for large left and right
        mid = left + (right - left) // 2; 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, left, mid); 
        merge_sort_in_place(arr, mid + 1, right); 
  
        merge_in_place(arr, left, mid, right); 

