""" 
Maximum and Minimum numbers Module.

Module provides a function to find the maximum and minimum numbers.
"""
values = (5, 67, 90, 5600, 1, 200, 500)

def check_max_min(numbers):
    """
    Check which one is the maximum and minimum numbers.

    Args:
        numbers (tuple): The numbers to be checked to find the maximum and minimum.

    Returns:
        tuple: A tuple containing the maximum and minimum numbers using both
               built-in functions and custom logic.
    """
    # Using built-in functions
    max_number = max(numbers)
    min_number = min(numbers)
    # Using custom logic
    custom_max = numbers[0]
    custom_min = numbers[0]

    for num in numbers:
        if num > custom_max:
            custom_max = num
        if num < custom_min:
            custom_min = num
    return (max_number, min_number), (custom_max, custom_min)

built_in_max_min, custom_max_min = check_max_min(values)

print("Using built-in functions")
print("Maximum number:", built_in_max_min[0])
print("Minimum number:", built_in_max_min[1])

print("\nUsing custom logic")
print("Maximum number:", custom_max_min[0])
print("Minimum number:", custom_max_min[1])
