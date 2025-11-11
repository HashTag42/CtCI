'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth element of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
from typing import Optional
from LinkedList import Node


def get_length(head: Optional[Node]) -> int:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def intersection(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
    """Return the intersecting node if two lists share a node by reference."""
    """Complexity: Time: O(n+m), Space: O(1)"""
    if not head1 or not head2:
        return None
    len1, len2 = get_length(head1), get_length(head2)
    cur1, cur2 = head1, head2
    if len1 > len2:
        for _ in range(len1 - len2):
            cur1 = cur1.next
    else:
        for _ in range(len2 - len1):
            cur2 = cur2.next
    while cur1 and cur2:
        if cur1 is cur2:
            return cur1
        cur1, cur2 = cur1.next, cur2.next
    return None
