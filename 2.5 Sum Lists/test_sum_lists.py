from sum_lists import sum_lists, get_val_from_reversed_ll, get_reversed_ll_from_val
from LinkedList import LinkedList
import pytest

test_sum_lists_cases = [
    ([0], [0], [0]),
    ([1], [2], [3]),
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([9, 9, 9], [1], [0, 0, 0, 1]),
    ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1]),
]


@pytest.mark.parametrize("list1, list2, expected", test_sum_lists_cases)
def test_sum_lists(list1, list2, expected):
    assert sum_lists(LinkedList(list1), LinkedList(list2)).to_list() == expected


get_val_from_reversed_ll_cases = [
    ([7, 1, 6], 617),
    ([3, 2, 1], 123),
]


@pytest.mark.parametrize("_list, expected", get_val_from_reversed_ll_cases)
def test_get_val_from_reversed_ll(_list, expected):
    ll = LinkedList(_list)
    assert get_val_from_reversed_ll(ll) == expected


get_reversed_ll_from_val_cases = [
    (617, [7, 1, 6]),
    (123, [3, 2, 1]),
]


@pytest.mark.parametrize("value, expected", get_reversed_ll_from_val_cases)
def test_get_reversed_ll_from_val(value, expected):
    assert get_reversed_ll_from_val(value).to_list() == expected
