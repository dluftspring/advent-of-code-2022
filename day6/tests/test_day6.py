import os
from common.utils import load_data
from day6 import find_unique_sub_sequence

TEST_DATA = list(load_data(os.path.join(os.path.dirname(__file__), "test-input.txt")))

def test_unique_sub_sequence():
    results = []
    for line in TEST_DATA:
        results.append(find_unique_sub_sequence(line.strip(), 4))

    assert results == [
        5,
        6,
        10,
        11
    ]