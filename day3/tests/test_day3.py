from day3 import (
    load_data,
    calculate_total_priority_by_line,
    calculate_total_priority_by_group,
    split_string_in_half,
    get_distinct_characters,
    find_all_matching_characters
    )

def test_calculate_total_priority_by_line():
    """
    Test total priority calculation
    """
    data = load_data('tests/test-input.txt')
    assert calculate_total_priority_by_line(data) == 157

def test_calculate_total_priority_by_group():
    """
    Test total priority calculation
    """
    data = load_data('tests/test-input.txt')
    assert calculate_total_priority_by_group(data) == 70

def test_split_string_in_half():
    """
    Test string splitting
    """
    assert split_string_in_half('abcdef') == ('abc', 'def')

def test_find_matched_characters():
    """
    Test finding matching characters in two string sequences
    """
    data = load_data('tests/test-input.txt')
    output_to_check = []
    for line in data:
        sequence_a, sequence_b = split_string_in_half(line.strip())
        distinct_characters = get_distinct_characters(sequence_a)
        output_to_check.extend(list(find_all_matching_characters(distinct_characters, sequence_b)))

    assert output_to_check == ['p', 'L', 'P', 'v', 't', 's']



