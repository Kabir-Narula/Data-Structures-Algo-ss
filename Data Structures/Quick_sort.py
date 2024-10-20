def quick_sort(lst):
    # Base case: A list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst

    # Recursive case: Choose a pivot and partition the list into two halves
    pivot = lst[len(lst) // 2]  # Choose the middle element as the pivot
    left = [x for x in lst if x < pivot]  # All elements less than the pivot
    middle = [x for x in lst if x == pivot]  # All elements equal to the pivot
    right = [x for x in lst if x > pivot]  # All elements greater than the pivot

    # Recursively sort the left and right parts, and then combine them
    return quick_sort(left) + middle + quick_sort(right)

# Example to test the function
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)

# Time Complexity:
# - Best-case and Average-case: O(n log n), where n is the number of elements in the list.
#   In the average and best-case scenarios, the pivot divides the list into two roughly equal halves.
#   Since we divide the list at each step (log n steps), and for each step, we perform linear work 
#   (comparing and partitioning n elements), the overall time complexity is O(n log n).
# - Worst-case: O(n²), which occurs when the pivot is the smallest or largest element, leading to highly unbalanced partitions. 
#   In this case, one of the partitions is empty, and the other contains n-1 elements, making the depth of the recursion linear (n).

# Space Complexity:
# - Best-case: O(log n), which is the space required for the recursion stack in the average and best cases when the list is evenly split.
# - Worst-case: O(n), which happens in the worst-case scenario when the pivot consistently divides the list into highly unbalanced partitions.
#   The recursive stack can grow to the size of the input list, leading to O(n) space complexity.

# Why Use Quick Sort?
# - Quick Sort is an **in-place** sorting algorithm, meaning it doesn’t require additional space proportional to the input size.
#   It only requires space for the recursion stack, making it more space-efficient than Merge Sort.
# - It is generally faster than other O(n log n) algorithms (such as Merge Sort) in practice, due to lower constant factors.
# - Quick Sort is widely used due to its excellent average-case performance and in-place nature.
# - However, its worst-case time complexity of O(n²) is a drawback, though this can be mitigated by using randomized pivots.

# Example of Execution:
# For the input list [38, 27, 43, 3, 9, 82, 10]:
# - The pivot is chosen as 43 (the middle element), and the list is partitioned into:
#   - Left: [38, 27, 3, 9, 10] (elements less than 43)
#   - Middle: [43] (elements equal to 43)
#   - Right: [82] (elements greater than 43)
# - The left and right partitions are recursively sorted. In the next level:
#   - Left partition [38, 27, 3, 9, 10] chooses 3 as the pivot, further partitioning into:
#     - Left: [] (empty)
#     - Middle: [3]
#     - Right: [38, 27, 9, 10]
#   - These partitions are further sorted, and so on, until the entire list is sorted as [3, 9, 10, 27, 38, 43, 82].
