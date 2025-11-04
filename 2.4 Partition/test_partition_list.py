from LinkedList import LinkedList
from partition_list import partition_list
import pytest


cases = [
    ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10]),
]


@pytest.mark.parametrize("linked_list, partition, expected", cases)
def test_partition(linked_list, partition, expected):
    ll = LinkedList(linked_list)
    ll = partition_list(ll, partition)
    assert ll.to_list() == expected
