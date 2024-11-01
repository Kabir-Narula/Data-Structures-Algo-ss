def linear_search(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            return f"{key} was found at index {i}"  # Proper string formatting
    return "element not found"  # Return this only if the element is not found after the loop

my_list = [2, 6, 8, 9, 3, 4]

print(linear_search(my_list, 4))
