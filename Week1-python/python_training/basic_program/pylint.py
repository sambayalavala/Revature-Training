"""
This module demonstrates adding two numbers using a function
and printing the result.
"""

def add_numbers(num1, num2):
    """
    Add two numbers and return the result.

    Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

if __name__ == "__main__":
    result = add_numbers(10, 20)
    print(result)

