from remove_dups import remove_dups1, remove_dups2
import pytest


common_cases = [
    # linked_list, expected
    ([], []),                                           # Empty list
    ([1], [1]),                                         # One item, no dup
    ([1, 1], [1]),                                      # One dup
    (["A", "B", "C", "D"], ["A", "B", "C", "D"]),       # No dups
]


cases_remove_dups1 = [
    # linked_list, expected
    ([1, 2, 3, 2], [1, 3, 2]),                          # One dup
    ([1, 2, 3, 1, 4, 1], [2, 3, 4, 1]),                 # Two dups
]


cases_remove_dups2 = [
    # linked_list, expected
    ([1, 2, 3, 2], [1, 2, 3]),                          # One dup
    ([1, 2, 3, 1, 4, 1], [1, 2, 3, 4]),                 # Two dups
]


@pytest.mark.parametrize("linked_list, expected", common_cases + cases_remove_dups1)
def test_remove_dups1(linked_list, expected):
    assert remove_dups1(linked_list) == expected


@pytest.mark.parametrize("linked_list, expected", common_cases + cases_remove_dups2)
def test_remove_dups2(linked_list, expected):
    assert remove_dups2(linked_list) == expected
