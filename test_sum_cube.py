"""
Test contains test cases for the functions in sum_cube.py using pytest.

Module provides test to calculate the sum of cube of specified number.
"""
from sum_cube import sum_of_cube

def test_sum_of_cube_with_positive_integer():
    """
    To test the sum of cube (3) is 1**3 + 2**3.

    Examples:
    - For the input 3, the expected result is 9, as 1^3 + 2^3 = 9.
    """
    # The sum of cubes of 1 and 2 is 1 + 8 = 9
    assert sum_of_cube(3) == 1**3 + 2**3, "Tested Successfully!"

def test_sum_of_cube_with_large_positive_integer():
    """
    Test for sum of cube of number 5 is 1**3 + 2**3 + 3**3 + 4**3

    Examples:
    - For the input 5, the expected result is 100, as 1^3 + 2^3 + 3^3 + 4^3 = 100.
    """
    # The sum of cubes of 1, 2, 3, and 4 is 1 + 8 + 27 + 64 = 100
    assert sum_of_cube(5) == 1**3 + 2**3 + 3**3 + 4**3, "Tested Successfully!"

# Run: pytest -s .\test_sum_cube.py
