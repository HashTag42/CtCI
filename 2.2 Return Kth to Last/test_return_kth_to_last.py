from return_kth_to_last import return_Kth_to_last
from LinkedList import LinkedList
import pytest


positive_cases = [
    # list, Kth, expected
    ([0], 0, 0),
    ([1, 2, 3, 4, 5], 0, 5),
    ([1, 2, 3, 4, 5], 1, 4),
    ([1, 2, 3, 4, 5], 2, 3),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 4, 1),
]


@pytest.mark.parametrize("list, Kth, expected", positive_cases)
def test_return_Kth_to_last(list, Kth, expected):
    linked_list = LinkedList(list)
    assert return_Kth_to_last(linked_list, Kth) == expected


negative_cases = [
    # list, Kth, expected
    ([], 0, ValueError),
    ([1, 2, 3, 4, 5], -1, ValueError),
    ([1, 2, 3, 4, 5], 5, ValueError),
]


@pytest.mark.parametrize("list, Kth, expected", negative_cases)
def test_return_Kth_to_last_exceptions(list, Kth, expected):
    linked_list = LinkedList(list)
    with pytest.raises(expected):
        return_Kth_to_last(linked_list, Kth)
