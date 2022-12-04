import os
import sys
import datetime
from typing import Generator

def load_data(file_path: os.PathLike = None, day: int = None) -> Generator:
    """
    Return a generator of each line in the input file
    """

    if not day:
        day = datetime.datetime.now().day

    if not file_path:
        file_path = f'day{day}/input/input{day}.txt'

    with open(file_path) as f:
        for line in f.readlines():
            yield line