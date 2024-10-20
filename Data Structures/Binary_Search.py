def binary(array, target):
    left = 0  # Starting index
    right = len(array) - 1  # Rightmost index of array
    
    while left <= right:
        mid = (left + right) // 2  # Use integer division to get the middle index
        
        if array[mid] == target:
            return mid  # Return the index of the target
        
        elif target < array[mid]:
            right = mid - 1  # Focus on the left half
            
        else:
            left = mid + 1  # Focus on the right half
    
    return -1  # Target not found

# Example array (must be sorted for binary search)
my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target to search for
target = 9

# Call the binary search function
result = binary(my_array, target)

# Print the result
if result != -1:
    print(f"Element {target} is found at index {result}.")
else:
    print(f"Element {target} is not found in the array.")

# Binary search is used to search in an sorted array or list, It usee O(log n) time complexity
# as it returns divides the array into smaller array checking if the target matches the middle index
# Binary search only uses a few extra variables (left, right, mid), so its space complexity is O(1). This means the space used doesn't change with the size of the input list.