# 2. Revise the Fibonacci program so that it asks the user for which
# Fibonacci number he or she wants. Then use this value to instead
# of 6 in the program. Use your program to compute the 10th, 20th,
# 30th and 40th Fibonacci numbers. Why does it take so much
# longer to computer the higher Fibonacci numbers? 

def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

n = int(input("Enter which Fibonacci number you want to compute: "))
print(f"The Fibonacci number at position {n} is: {fibonacci(n)}")
