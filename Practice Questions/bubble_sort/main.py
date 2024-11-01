def bubble_sort(items):
    length = len(items)
    for i in range(length):
        for j in range(length - i - 1):
            if items[j] > items[j + 1]:  
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap elements

# Example usage
items = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(items)
print(items)
