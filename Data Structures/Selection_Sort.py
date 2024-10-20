def selection_sort(lst):
    # Outer loop to control the number of passes through the list
    for i in range(len(lst) - 1):  # Iterate over all elements except the last one
        min_idx = i  # Assume the current position is the minimum (start of the unsorted portion)

        # Inner loop to find the minimum element from the unsorted part of the list
        for j in range(i + 1, len(lst)):
            # Compare each element in the unsorted part with the current minimum
            if lst[j] < lst[min_idx]:
                # If a smaller element is found, update the index of the minimum element
                min_idx = j

        # If the minimum element is not at the current position (i), swap it with the element at index i
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]  # Swap the elements

# Example to test the function
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted list:", my_list)

# Time Complexity: 
# - Worst-case and Average-case: O(n²), where n is the number of elements in the list.
#   The outer loop runs (n - 1) times, and for each iteration, the inner loop runs (n - i - 1) times,
#   leading to a total of n*(n-1)/2 comparisons, which simplifies to O(n²).
#   For example, for a list of 5 elements, the total comparisons will be 4 + 3 + 2 + 1 = 10 comparisons.

# Space Complexity: 
# - O(1) (constant space), because the sorting is done in-place. No additional space proportional 
#   to the input size is required, aside from the input list itself. The only additional variables used 
#   are min_idx and loop counters.

# Why Use Selection Sort?
# - In-place sorting: Selection Sort does not require any additional memory, making it suitable 
#   when memory usage is limited.
# - Simple to implement: It is easy to understand and implement, especially when sorting small lists.
# - Drawbacks: While simple, its time complexity of O(n²) makes it inefficient for large lists compared 
#   to more advanced sorting algorithms like Merge Sort or Quick Sort.

# Example of Execution:
# For the input list [64, 25, 12, 22, 11]:
# - First pass (i=0): Find the minimum (11), swap with 64 -> [11, 25, 12, 22, 64]
# - Second pass (i=1): Find the minimum (12), swap with 25 -> [11, 12, 25, 22, 64]
# - Third pass (i=2): Find the minimum (22), swap with 25 -> [11, 12, 22, 25, 64]
# - Fourth pass (i=3): Find the minimum (25) is already in place, no swap needed -> [11, 12, 22, 25, 64]
# The final sorted list is [11, 12, 22, 25, 64].
