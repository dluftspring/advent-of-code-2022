import os
import re
from typing import Iterable, List
from common.utils import load_data
from collections import defaultdict

def create_dict_of_crates(data: Iterable) -> dict:

    """
    Take input data and return a dictionary keyed by column position with a variable
    list of crates depending on the input file
    """

    dict_of_crates = defaultdict(list)
    for line in data:
        if line == '\n' or '1' in line:
            break
        idx = 1
        line = line.replace('\n','')
        for location in range(0, len(line), 4):
            crate = line[location:location+4].strip()
            if crate:
                dict_of_crates[idx].insert(0, crate.replace('[','').replace(']',''))
            idx += 1

    return dict_of_crates

def get_movement_instructions(data: Iterable) -> List[list]:

    """
    Take list of instructions and return list of movement instructions
    Only the integer componennts of the instructions are returned
    """

    movement_instructions = []
    for line in data:
        if '[' in line or line.strip().startswith('1') or not line.strip():
            continue
        else:
            list_of_instructions = re.split('(\d+)', line)
            movement_instructions.append([int(x) for x in list_of_instructions if x.isdigit()])

    return movement_instructions




def arrange_crates(dict_of_crates: dict, movement_instructions: Iterable, crate_mover: int) -> dict:
    """
    Return dict of crates after the movement instructions
    """

    for instruction in movement_instructions:
        if instruction:
            num_crates = instruction[0]
            start_pos = instruction[1]
            end_pos = instruction[2]
            crates_to_move = dict_of_crates[start_pos][-num_crates:]
            if crate_mover == 9000:
                crates_to_move.reverse()
            dict_of_crates[end_pos].extend(crates_to_move)
            crates_to_keep = len(dict_of_crates[start_pos]) - num_crates
            dict_of_crates[start_pos] = dict_of_crates[start_pos][:crates_to_keep]

    return dict_of_crates

def show_top_level_crates(dict_of_crates: dict) -> List:
    """
    Return list of top level crates
    """

    top_level_crates = ''
    for _, value in sorted(dict_of_crates.items()):
        if value:
            top_level_crates+=value[-1]

    return top_level_crates




if __name__ == "__main__":
    data = list(load_data(os.path.join(os.path.dirname(__file__), 'input/input5.txt')))
    dict_of_crates = create_dict_of_crates(data)
    print(dict_of_crates)
    movement_instructions = get_movement_instructions(data)
    arranged_crates = arrange_crates(dict_of_crates, movement_instructions, crate_mover=9001)
    print(f"The top level crates after movement are: {show_top_level_crates(arranged_crates)}")