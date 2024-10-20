def linear(array, target):
    # Iterate over the list and check each element
    for i in range(len(array)):
        if array[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Use a list instead of a set
my_array = [2, 6, 8, 9, 3, 4]

target = 2  # The element to search for

# Perform the linear search
result = linear(my_array, target)

# Print the result
if result != -1:
    print(f"Element {target} is found at index {result}.")
else:
    print(f"Element {target} is not found in the array.")
    
# Linear search is used to search in an unsorted array or list, It usee O(n) time complexity
# as it checks each element in the list to see if it matches the target element
# Linear search uses a single loop to iterate over the list, so its space complexity is O(1). This means the space used doesn't change with the size of the input list.