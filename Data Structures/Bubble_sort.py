def bubble_sort(items):
    # Outer loop to control the number of passes through the array
    for i in range(len(items)):
        # Inner loop to compare adjacent elements and perform swaps
        # After each pass, the largest element in the unsorted portion 'bubbles' up to its correct position
        for j in range(len(items) - 1 - i):
            # Compare the current element with the next one in the list
            if items[j] > items[j + 1]:
                # If the current element is larger than the next one, swap them
                # This ensures that the larger element moves toward the end of the list
                items[j], items[j + 1] = items[j + 1], items[j]
                
# Example to test the function
my_list = [5, 3, 8, 4, 2]
bubble_sort(my_list)
print("Sorted list:", my_list)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Explanation:
# The time complexity is O(n^2) because there are two nested loops, and in the worst case, we will make comparisons for each pair of elements in the list.
# The space complexity is O(1) because bubble sort sorts the list in place, without requiring any additional space other than a few variables for swapping.
