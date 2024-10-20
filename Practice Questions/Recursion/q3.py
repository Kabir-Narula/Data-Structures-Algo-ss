# #4. (HARDER) Write a recursive Python function that has a parameter representing a list of integers and returns the maximum stored in the list. Thinking recursively, the maximum is either the

# First value in the list or the maximum of the rest of the list,whichever is larger. If the list only has 1 integer, then its maxim is this single value, naturally.

# Helpful Python syntax:
# If A is a list of integers, and you want to set the list B to all of the integers in A except the first one, you can write
# B = A[1:len(A)]
# (This sets B to the integers in A starting at index 1 and ending at index len(A)-1, the last index. The integer in the first position of A at index 0 is not included.)


def find_max_in_list(lst):
    # Check if input is a list and if it's empty
    if not isinstance(lst, list) or len(lst) == 0:
        return "Invalid arguments"

    # Base case: if the list has only one element, return that element
    elif len(lst) == 1:
        return lst[0]
    
    # Recursive case: find the maximum of the rest of the list
    else:
        max_of_rest = find_max_in_list(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

# Test the function
print(find_max_in_list([3, 1, 4, 1, 5, 9, 2, 6]))  # Output: 9
print(find_max_in_list([10]))                      # Output: 10
print(find_max_in_list([]))                        # Output: Invalid arguments

