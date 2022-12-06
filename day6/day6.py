from common.utils import load_data
from typing import Generator

def  find_unique_sub_sequence(sequence: str, length_of_sequence: int) -> int:
    """
    Given a sequence of characters and a length of sequence, find the first occurence of
    a unique subsequences of the given length
    """

    for idx in range(0, len(sequence) - length_of_sequence + 1):
        sub_sequence = sequence[idx:idx+length_of_sequence]
        if len(set(sub_sequence)) == length_of_sequence:
            return idx + length_of_sequence

if __name__ == "__main__":
    data = load_data()
    for line in data:
        # print(f"The first start-of-packet marker occurs at: {find_unique_sub_sequence(line.strip(), 4)}")
        print(f"The first start-of-message marker occurs at: {find_unique_sub_sequence(line.strip(), 14)}")