import os
from typing import Iterable, Generator

def load_data(file_path: os.PathLike = None) -> Generator:
    """
    Return a generator of each line in the input file
    """

    if not file_path:
        file_path = os.path.join(os.path.dirname(__file__), 'input/input1.txt')

    with open(file_path) as f:
        for line in f.readlines():
            yield line

def count_calories_per_elf(data: Iterable) -> int:
    """
    Count the calories in the data set. Each blank line represents a new elf
    This should return the total calories of the elf with the highest score
    """

    elves = {}
    elf_number = 1
    calory_count = 0

    for calories in data:

        if calories != '\n':
            calory_count += int(calories)
            elves[elf_number] = calory_count

        if calories == '\n':
            elf_number += 1
            calory_count = 0

    return max(elves.values()), elves

def find_top_n_elves(data: Iterable, n: int = 3) -> int:
    """
    Find the top N elves with the highest calorie count
    """

    _, elves = count_calories_per_elf(data)
    return sorted(elves.values(), reverse=True)[:n]


if __name__ == "__main__":
    result, _ = count_calories_per_elf(load_data())
    print(f"The elf with the most calories is: {result}")

    top_3_elves = find_top_n_elves(load_data(), 3)
    print(f"The top 3 elves have a combined total of {sum(top_3_elves)} calories")
