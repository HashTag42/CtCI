from intersection import intersection
from LinkedList import LinkedList
import pytest

cases = [
    # list1, list2, expected
    # Positive cases
    ([1], [1], 1),
    ([1, 9], [2, 9], 9),
    ([1, 9, 3], [2, 9, 3], 9),
    ([1, 9, 2], [3, 4, 9, 2], 9),
    ([3, 1, 5, 9, 7, 2, 1], [4, 6, 7, 2, 1], 7),
    # Negative cases
    ([1], [2], None),
    ([1], [1, 2], None),
    ([1, 9, 3], [2, 9, 3, 4], None),
]


@pytest.mark.parametrize("list1, list2, expected", cases)
def test_intersection(list1, list2, expected):
    assert intersection(LinkedList(list1), LinkedList(list2)) == expected
