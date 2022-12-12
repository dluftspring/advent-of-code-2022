import os
from common.utils import load_data
from day7 import DirectoryWalker

TEST_DATA = load_data(os.path.join(os.path.dirname(__file__), "test-input.txt"))

def test_total_size():
    walker = DirectoryWalker(TEST_DATA)
    walker.walk()
    assert walker.dir_size['/'] == 48381165