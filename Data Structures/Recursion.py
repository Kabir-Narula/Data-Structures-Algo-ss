# Function to calculate the factorial of a number using recursion
def recursion(n):
    # Base case: If n == 0, return 1 (since 0! = 1)
    # This is the termination condition for the recursion.
    if n == 0:
        return 1
    else:
        # Recursive case: Return n * factorial of (n-1)
        # This is the recursive step that continues until n reaches 0.
        return n * recursion(n-1)

# Test the function with n = 5
result = recursion(5)  # This will calculate the factorial of 5, i.e., 5!
print(f"The factorial of 5 is: {result}")

# Time Complexity: O(n)
# Explanation:
# Each recursive call reduces n by 1, resulting in n recursive calls before reaching the base case (n == 0).
# The work done at each call is constant (just multiplication), so the total time complexity is O(n).

# Space Complexity: O(n)
# Explanation:
# The space complexity is determined by the maximum depth of the recursive call stack.
# Since the function calls itself n times (from n to 0), the maximum depth of the call stack will be n.
# Therefore, the space complexity is O(n), which is the depth of the recursion tree.
