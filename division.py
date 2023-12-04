"""
Divisible check Module.

Module provides a function to check whether a number is divisible by another number.
"""
def is_divisible(number, divisor):
    """
    Check if a number is divisible by another number.

    Args:
        number (integer): The number to be checked.
        divisor (integer): The divisor.

    Returns:
        bool: True if the number is divisible by the divisor, False otherwise.
    """
    return number % divisor == 0

result = is_divisible(12, 6)
print(result)
    
