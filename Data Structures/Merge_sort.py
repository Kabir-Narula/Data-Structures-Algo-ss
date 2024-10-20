def merge_sort(lst):
    # Base case: If the list is of length 1 or 0, it is already sorted
    if len(lst) <= 1:
        return lst

    # Recursive case: Split the list into two halves
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])  # Recursively sort the left half
    right_half = merge_sort(lst[mid:])  # Recursively sort the right half

    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []  # Temporary list to hold the merged and sorted elements
    i = j = 0  # Pointers for left and right halves

    # Merge the two lists until one is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])  # Add the smaller element from the left half
            i += 1
        else:
            sorted_list.append(right[j])  # Add the smaller element from the right half
            j += 1

    # Append any remaining elements from the left and right halves
    sorted_list.extend(left[i:])  # If left list has remaining elements, append them
    sorted_list.extend(right[j:])  # If right list has remaining elements, append them

    return sorted_list

# Example to test the function
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print("Sorted list:", sorted_list)

# Time Complexity:
# - Worst-case and Average-case: O(n log n), where n is the number of elements in the list.
#   Merge Sort divides the list in half at each step, which creates a logarithmic depth of recursive calls (log n).
#   Each level of the recursion performs a linear amount of work (O(n)) to merge the sublists.
#   Therefore, the overall time complexity is O(n log n).
#   Example: For a list of 8 elements, we divide it until we have individual elements (log₂8 = 3 steps) 
#   and at each step, we merge (linear work) the divided lists.

# Space Complexity:
# - O(n), because merge sort uses additional memory to store the temporary lists created 
#   during the splitting and merging process. Each recursive call creates new lists, and during merging, 
#   temporary lists are created for each level of recursion.
#   Although the space complexity is linear, it is higher than in-place sorting algorithms like Quick Sort 
#   (O(log n) space), which makes Merge Sort less space-efficient.

# Why Use Merge Sort?
# - Stable sort: Merge Sort is a stable algorithm, meaning it maintains the relative order of elements with equal keys.
# - Guaranteed O(n log n): Unlike Quick Sort, which can degrade to O(n²) in the worst case, Merge Sort consistently 
#   performs at O(n log n), making it a good choice when performance guarantees are required.
# - Drawbacks: It uses extra space (O(n)) due to the auxiliary arrays used during the merge process, making it less 
#   efficient in terms of memory usage for very large datasets compared to in-place sorting algorithms.

# Example of Execution:
# For the input list [38, 27, 43, 3, 9, 82, 10]:
# - First, it splits into [38, 27, 43] and [3, 9, 82, 10].
# - Then [38, 27, 43] splits into [38] and [27, 43], and [27, 43] further splits into [27] and [43].
# - Similarly, [3, 9, 82, 10] splits into [3, 9] and [82, 10], and so on.
# - After reaching individual elements, the algorithm merges them back into sorted order:
#   [27, 38, 43] and [3, 9, 10, 82].
# - Final merge results in [3, 9, 10, 27, 38, 43, 82].
