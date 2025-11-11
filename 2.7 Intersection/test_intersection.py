from LinkedList import LinkedList
from intersection import intersection


def test_no_intersection():
    head1 = LinkedList([1, 2, 3]).head
    head2 = LinkedList([4, 5, 6]).head
    assert intersection(head1, head2) is None


def test_intersection_at_middle_len1_greater_than_len2():
    # Shared tail
    shared = LinkedList([7, 8, 9]).head
    head1 = LinkedList([1, 2, 3]).head
    head2 = LinkedList([4, 5]).head

    # Attach shared tail
    cur = head1
    while cur.next:
        cur = cur.next
    cur.next = shared

    cur = head2
    while cur.next:
        cur = cur.next
    cur.next = shared

    # Intersection should be the first shared node
    result = intersection(head1, head2)
    assert result is shared


def test_intersection_at_middle2_len2_greater_than_len1():
    # Shared tail
    shared = LinkedList([7, 8, 9]).head
    head1 = LinkedList([1, 2]).head
    head2 = LinkedList([4, 5, 6]).head

    # Attach shared tail
    cur = head1
    while cur.next:
        cur = cur.next
    cur.next = shared

    cur = head2
    while cur.next:
        cur = cur.next
    cur.next = shared

    # Intersection should be the first shared node
    result = intersection(head1, head2)
    assert result is shared


def test_intersection_at_head():
    # Both lists are literally the same list
    head = LinkedList([1, 2, 3]).head
    assert intersection(head, head) is head


def test_empty_lists():
    assert intersection(None, None) is None
    assert intersection(LinkedList([1, 2]).head, None) is None
    assert intersection(None, LinkedList([3, 4]).head) is None
