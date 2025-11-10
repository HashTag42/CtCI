from intersection import intersection
from LinkedList import LinkedList
import pytest

intersection_cases = [
    # list1, list2, expected
    # Positive cases
    ([1], [1], 1),
    ([1, 9], [2, 9], 9),
    ([1, 9, 3], [2, 9, 3], 9),
    ([1, 9, 2], [3, 4, 9, 2], 9),
    ([3, 1, 5, 9, 7, 2, 1], [4, 9, 6, 7, 2, 1], 7),
    # Negative cases
    ([], [], None),
    ([1], [2], None),
    ([1], [1, 2], None),
    ([1, 9, 3], [2, 9, 3, 4], None),
]


@pytest.mark.parametrize("list1, list2, expected", intersection_cases)
def test_intersection(list1, list2, expected):
    actual = intersection(LinkedList(list1).head, LinkedList(list2).head)
    actual = actual.data if actual else None
    assert actual == expected
