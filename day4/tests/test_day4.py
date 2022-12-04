import os
from day4 import (
    load_data,
    convert_string_range_to_numeric,
    is_either_range_a_subset,
    is_either_range_overlapping,
    calculate_overlapping_assignments
)

TEST_DATA = list(load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt')))

def test_convert_string_range_to_numeric():
    assert convert_string_range_to_numeric('1-3') == range(1, 4)

def test_is_either_range_a_subset():
    assert is_either_range_a_subset(range(1, 4), range(1, 5))
    assert not is_either_range_a_subset(range(1, 4), range(2, 5))

def test_is_either_range_overlapping():
    assert not is_either_range_overlapping(range(1, 4), range(5, 7))
    assert is_either_range_overlapping(range(1, 4), range(3, 5))

def test_calculate_overlapping_assignments():
    assert calculate_overlapping_assignments(TEST_DATA, how='subset') == 2
    assert calculate_overlapping_assignments(TEST_DATA, how='overlapping') == 4