import os
from day1 import load_data, count_calories_per_elf

def test_max():
    data = load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt'))
    result, _ = count_calories_per_elf(data)
    assert result == 650

def test_number_of_elves():
    data = load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt'))
    _, elves = count_calories_per_elf(data)
    assert len(elves) == 4

def test_calories_per_elf():
    data = load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt'))
    _, elves = count_calories_per_elf(data)
    assert elves[1] == 30
    assert elves[2] == 650
    assert elves[3] == 2
    assert elves[4] == 4