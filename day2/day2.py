import os
from typing import Iterable, Generator, List

def load_data(file_path: os.PathLike = None) -> Generator:
    """
    Return a generator of each line in the input file
    """

    if not file_path:
        file_path = os.path.join(os.path.dirname(__file__), 'input/input2.txt')

    with open(file_path) as f:
        for line in f.readlines():
            yield line

def get_total_score(data: Iterable, strategy: str) -> List[int]:

    """
    Calculate rock paper scissors score per line and return the sum of all scores

    A = Rock
    B = Paper
    C = Scissors

    X = Rock (1) + win/loss
    Y = Paper (2) + win/loss
    Z = Scissors (3) + win/loss

    """

    if strategy == 'explicit':

        # X = Rock A = Rock
        # Y = Paper B = Paper
        # Z = Scissors C = Scissors

        score_mapping = {
            'AX': 1+3,
            'AY': 2+6,
            'AZ': 3+0,
            'BX': 1+0,
            'BY': 2+3,
            'BZ': 3+6,
            'CX': 1+6,
            'CY': 2+0,
            'CZ': 3+3,
        }

    if strategy == 'implicit':

        # X = Loss A = Rock
        # Y = Draw B = Paper
        # Z = Win C = Scissors

        score_mapping = {
            'AX': 3+0,
            'AY': 1+3,
            'AZ': 2+6,
            'BX': 1+0,
            'BY': 2+3,
            'BZ': 3+6,
            'CX': 2+0,
            'CY': 3+3,
            'CZ': 1+6,
        }

    outcomes = map(lambda strategy: score_mapping.get(strategy.strip().replace(' ','')), data)
    return sum(outcomes)


if __name__ == '__main__':
    data = load_data()
    result = get_total_score(data, strategy='implicit')
    print(f"The total score from all games is: {result}")
