"""
Sum of cube of number Module.

Module provides a function to calculate the sum of the cube of all positive integers
"""
positive_number = int(input("Enter a positive integer: "))

def sum_of_cube(number):
    """
    Calculate the sum of the cube of positive integers up to the given number.

    Args:
        number (int): The positive integer up to which the sum of cubes will be calculated.

    Returns:
        int: The sum of the cubes of positive integers up to the given number.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Initialize the sum 0
    cube_sum = 0
    # Iterate the positive integers smaller than the number and add their cubes to sum
    for i in range(1, number):
        cube_sum += i ** 3
    return cube_sum

print("Sum of cubes of positive integer", positive_number, "is",  sum_of_cube(positive_number))
