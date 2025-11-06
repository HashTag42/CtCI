from isPalindrome import isPalindrome
from LinkedList import LinkedList
import pytest

cases = [
    # linked_list, expected
    # Positive cases
    (None, True),
    ([None], True),
    ([], True),
    ([1], True),
    [[1, 1], True],
    ([1, 2, 1], True),
    # Negative cases
    ([1, 2], False),
    ([1, 2, 3], False),
]


@pytest.mark.parametrize("linked_list, expected", cases)
def test_isPalindrome(linked_list, expected):
    ll = LinkedList(linked_list)
    assert isPalindrome(ll) == expected
