from common.utils import load_data
from typing import Iterable, Generator, List

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def split_string_in_half(sequence: str) -> List[str]:
    """
    Split a string in half
    """

    return sequence[:len(sequence)//2], sequence[len(sequence)//2:]

def get_distinct_characters(sequence: str) -> Generator:
    """
    Return a generator of distinct characters in a sequence
    """

    chars = []
    for character in sequence:
        if character not in chars:
            chars.append(character)
            yield character

def find_all_matching_characters(sequence_a: str, sequence_b: str) -> Generator:
    """
    Find all matching characters in two sequences
    """

    for character in sequence_a:
        if character in sequence_b:
            yield character

def calculate_total_priority_by_line(data: Iterable):

    """
    Calculate the total priority of all characters
    """

    total_priority = 0

    for line in data:
        sequence_a, sequence_b = split_string_in_half(line.strip())
        distinct_characters = get_distinct_characters(sequence_a)
        matched_items = list(find_all_matching_characters(distinct_characters, sequence_b))
        if matched_items:
            total_priority += ALPHABET.index(matched_items[0]) + 1

    return total_priority

def calculate_total_priority_by_group(data: Iterable):

    """
    Calculate the total priority of all characters
    """

    total_priority = 0

    # No generators allowed because we need lookaheads
    data_in_mem = list(data)

    for idx in range(0, len(data_in_mem), 3):
        sequence_a = data_in_mem[idx].strip()
        sequence_b = data_in_mem[idx+1].strip()
        sequence_c = data_in_mem[idx+2].strip()
        distinct_characters = get_distinct_characters(sequence_a)
        first_two = list(find_all_matching_characters(distinct_characters, sequence_b))
        if first_two:
            matched_items = list(find_all_matching_characters(first_two, sequence_c))
            if matched_items:
                total_priority += ALPHABET.index(matched_items[0]) + 1

    return total_priority

if __name__ == "__main__":
    data = load_data()
    print(f"The total prioirty of repeated items is {calculate_total_priority_by_group(data)}")
