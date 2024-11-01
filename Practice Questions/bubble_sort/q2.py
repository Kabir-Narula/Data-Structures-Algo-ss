# 2. Medium:
# Modify the bubble sort algorithm so that it stops early if the list becomes sorted before completing all iterations. This is an optimization known as the "optimized bubble sort".

# For example, for the list:

# python
# Copy code
# numbers = [3, 2, 1, 8, 5, 6, 9]
# The optimized bubble sort should stop early after the second pass when no swaps are needed.

# Task: Implement an optimized version of bubble sort that detects if no swaps were made during a pass, and stops the algorithm early.

def optimized_bubble_sort(items):
    n = len(items)
    for i in range(n):
        swapped = False  # Flag to track if any swaps occurred in this pass
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                # Swap the elements
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True  # Set flag since a swap occurred
        if not swapped:
            # No swaps occurred; the list is sorted
            return "already sorted, no swap needed"
    return items  # Return the sorted list after all passes
