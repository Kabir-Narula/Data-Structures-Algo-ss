# Write a Python function using bubble sort to sort the following list in ascending order:

# numbers = [5, 1, 4, 2, 8]

def bubble_sort(items):
    length = len(items)
    for i in range(length):
        for j in range(length - i - 1):
            if items[j] > items[j + 1]:  
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap elements

# Example usage
numbers = [5, 1, 4, 2, 8]
bubble_sort(numbers)
print(numbers)
