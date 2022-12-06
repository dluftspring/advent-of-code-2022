import os
from common.utils import load_data
from day5 import (
    create_dict_of_crates,
    get_movement_instructions,
    arrange_crates,
    show_top_level_crates
)

TEST_DATA = list(load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt')))

def test_get_dict_of_crates():

    dict_of_crates = create_dict_of_crates(TEST_DATA)
    assert dict_of_crates == {
        1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P']
    }

def test_get_movement_instructions():

    movement_instructions = get_movement_instructions(TEST_DATA)
    assert movement_instructions == [
        [1, 2, 1],
        [3, 1, 3],
        [2, 2, 1],
        [1, 1, 2]
    ]

def test_arrange_crates_9000():

    dict_of_crates = create_dict_of_crates(TEST_DATA)
    movement_instructions = get_movement_instructions(TEST_DATA)
    arranged_crates = arrange_crates(dict_of_crates, movement_instructions, crate_mover=9000)
    assert arranged_crates == {
        1: ['C'],
        2: ['M'],
        3: ['P', 'D', 'N', 'Z']
    }

def test_arrange_crates_9001():

    dict_of_crates = create_dict_of_crates(TEST_DATA)
    movement_instructions = get_movement_instructions(TEST_DATA)
    arranged_crates = arrange_crates(dict_of_crates, movement_instructions, crate_mover=9001)
    assert arranged_crates == {
        1: ['M'],
        2: ['C'],
        3: ['P', 'Z', 'N', 'D']
    }