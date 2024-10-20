#1. Write a Python program to calculate the sum of a list of numbers using recursion.

def sum(n):
  if len(n) == 0:
    return 0
  else:
    return n[0] + sum(n[1:])


print (sum([1, 2, 3]))