from delete_middle_node import delete_middle_node
from LinkedList import LinkedList
import pytest


cases = [
    # nodes, value, expected
    ([1, 2, 3], 2, [1, 3]),
    ([1, 2, 3, 4, 5, 6], 3, [1, 2, 4, 5, 6]),
]


@pytest.mark.parametrize("nodes, value, expected", cases)
def test_delete_middle_node(nodes, value, expected):
    ll = LinkedList(nodes)

    current = ll.head
    while current:
        if current.data == value:
            break
        current = current.next

    delete_middle_node(current)
