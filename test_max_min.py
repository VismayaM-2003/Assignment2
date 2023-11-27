"""
Test contains test cases for the functions in max_min.py using pytest.

Provides test to find the maximum and minimum numbers from a sequence of numbers.
"""
from max_min import check_max_min

def test_check_max_min_1():
    """
    Test the maximum and minimum number for Test Case 1.

    Example:
    - Given the values (50000, 67, 90, 5600, 999, 200, 500),
      the expected result using built-in functions is (50000, 67),
      and the expected result using custom logic is (50000, 67).
    """
    # Test Case: 1
    test_1 = (50000, 67, 90, 5600, 999, 200, 500)
    built_in_max_min, custom_max_min = check_max_min(test_1)

    assert built_in_max_min == (50000, 67)
    assert custom_max_min == (50000, 67), "Tested Successfully!"

def test_check_max_min_2():
    """
    Test the maximum and minimum number for Test Case 2.

    Example:
    - Given the values (5, 67, 90000, 5600, 1, 200, 500),
      the expected result using built-in functions is (90000, 1),
      and the expected result using custom logic is (90000, 1).
    """
    # Test Case: 2
    test_2 = (5, 67, 90000, 5600, 1, 200, 500)
    built_in_max_min, custom_max_min = check_max_min(test_2)

    assert built_in_max_min == (90000, 1)
    assert custom_max_min == (90000, 1), "Tested Successfully!"

def test_check_max_min_3():
    """
    Test the maximum and minimum number for Test Case 3.

    Example:
    - Given the values (5, 67, 90, 5600, 1, 200, 500),
      the expected result using built-in functions is (5600, 1),
      and the expected result using custom logic is (5600, 1)
    """
    # Test Case: 3
    values_1 = (5, 67, 90, 5600, 1, 200, 500)
    built_in_max_min, custom_max_min = check_max_min(values_1)

    assert built_in_max_min == (5600, 1)
    assert custom_max_min == (5600, 1), "Tested Successfully!"
