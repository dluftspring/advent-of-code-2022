import os
import sys
from typing import Iterable
from common.utils import load_data

def convert_string_range_to_numeric(string_range: str) -> range:
    """
    Take a string range of the format
    1-3 and return a python range object of the same interval

    >>> convert_string_range_to_numeric('1-3')
    range(1, 4)
    """

    start, end = string_range.strip().split('-')
    return range(int(start), int(end) + 1)

def is_either_range_a_subset(range_a: range, range_b: range) -> bool:
    """
    Check if range_a is a subset of range_b

    >>> is_range_a_subset(range(1, 4), range(1, 5))
    True
    >>> is_range_a_subset(range(1, 4), range(2, 5))
    False
    """

    return set(range_a).issubset(range_b) or set(range_b).issubset(range_a)

def is_either_range_overlapping(range_a: range, range_b: range) -> bool:
    """
    Check if range_a is overlapping with range_b

    >>> is_either_range_overlapping(range(1, 4), range(1, 5))
    True
    >>> is_either_range_overlapping(range(1, 4), range(2, 5))
    True
    >>> is_either_range_overlapping(range(1, 4), range(5, 6))
    False
    """

    return bool(set(range_a).intersection(range_b))

def calculate_overlapping_assignments(data: Iterable, how: str) -> int:
    """
    Calculate number of overlapping assignments based on the
    pairs provided
    """

    strategy_map = {
        'subset': is_either_range_a_subset,
        'overlapping': is_either_range_overlapping
    }

    overlapping_assignments = 0
    for assignment in data:
        assignment_1, assignment_2 = assignment.split(',')
        range_1 = convert_string_range_to_numeric(assignment_1)
        range_2 = convert_string_range_to_numeric(assignment_2)
        if strategy_map[how](range_1, range_2):
            overlapping_assignments += 1

    return overlapping_assignments

if __name__ == '__main__':
    data = load_data(os.path.join(os.path.dirname(__file__), 'input/input4.txt'))
    # print(f"The number of fully contained assignments is: {calculate_overlapping_assignments(data, how='subset')}")
    print(f"The number of overlapping assignments is: {calculate_overlapping_assignments(data, how='overlapping')}")