"""
Test contains test cases for the functions in division.py using pytest.

Module provides test to whether a number is divisible by another number.
"""
from division import is_divisible

def test_is_divisible_by_even_number():
    """
    Testing the even number is divisible by another number.   

    Examples:
    - 8 is divisible by 2, so the result should be True.
    """
    assert is_divisible(8, 2) is True, "Tested Successfully!"

def test_is_divisible_by_odd_number():
    """
    Testing the odd number is divisible by another number.

    Examples:
    - 9 is divisible by 3, so the result should be True.
    """
    assert is_divisible(9, 3) is True, "Tested Successfully!"

def test_is_not_divisible():
    """
    Testing with non divisible number by another number.

    Examples:
    - 7 is not divisible by 3, so the result should be False.
    """
    assert is_divisible(7, 3) is False, "Tested Successfully!"
