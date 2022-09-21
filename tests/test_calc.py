import pytest 

from average_calculator.calc import rounded_average


def test_average_of_two_numbers_is_properly_computed():
    actual = rounded_average([4, 6])
    # Delete the skip and write the proper assertion here!
    assert actual == 5


def test_average_of_empty_list_raises_ValueError():
    # Delete the skip and write the test here!
    # Hint: use pytest.raises
   
    with pytest.raises(ValueError): 
        rounded_average([])