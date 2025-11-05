from sum_lists import sum_lists
from LinkedList import LinkedList
import pytest

cases = [
    ([0], [0], [0]),
    ([1], [2], [3]),
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([9, 9, 9], [1], [0, 0, 0, 1]),
    ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1]),
]


@pytest.mark.parametrize("list1, list2, expected", cases)
def test_sum_lists(list1, list2, expected):
    assert sum_lists(LinkedList(list1), LinkedList(list2)).to_list() == expected
