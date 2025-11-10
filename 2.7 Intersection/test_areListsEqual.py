from intersection import areListsEqual
from LinkedList import LinkedList
import pytest


areListsEqual_cases = [
    # Positive cases
    (None, None, True),
    ([], [], True),
    ([1], [1], True),
    ([1, 2, 3], [1, 2, 3], True),
    # Negative cases
    (None, [1], False),
    ([], [1], False),
    ([1], [2], False),
    ([1], [1, 2], False),
    ([1, 2], [1, 2, 3], False),
    ([1, 9, 3], [1, 2, 3], False),
]


@pytest.mark.parametrize("list1, list2, expected", areListsEqual_cases)
def test_areListsEqual(list1, list2, expected):
    assert areListsEqual(LinkedList(list1).head, LinkedList(list2).head) == expected
