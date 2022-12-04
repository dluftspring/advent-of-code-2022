import os
from day2 import load_data, get_total_score


def test_explicit_calculations():

    """
    Test win loss and draw calculations
    """

    data = load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt'))
    assert get_total_score(data, strategy='explicit') == 15

def test_implicit_calculations():

        """
        Test win loss and draw calculations
        """

        data = load_data(os.path.join(os.path.dirname(__file__), 'test-input.txt'))
        assert get_total_score(data, strategy='implicit') == 12

