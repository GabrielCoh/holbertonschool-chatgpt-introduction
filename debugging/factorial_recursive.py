#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number 'n' using recursion.
# The factorial of a number is the product of all positive integers less than or equal to that number.
# For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

# Parameters:
# - n (int): The number for which the factorial will be calculated.
#   n must be a non-negative integer (0, 1, 2, ...).

# Returns:
# - int: The factorial of the number 'n'.
#   If n is 0, the function will return 1, as 0! is defined to be 1.

def factorial(n):
    if n == 0:  # Base case: 0! = 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial(n-1)

f = factorial(int(sys.argv[1]))

print(f)

