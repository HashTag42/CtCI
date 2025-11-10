'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth element of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
from LinkedList import Node
from typing import Optional


def intersection(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
    cur1 = head1
    while cur1:
        cur2 = head2
        while cur2:
            if cur1.data == cur2.data:
                if areListsEqual(cur1, cur2):
                    return cur1
            cur2 = cur2.next
        cur1 = cur1.next
    return None


def areListsEqual(node1: Optional[Node], node2: Optional[Node]) -> bool:
    """
    Checks if two linked lists are identical.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    cur1, cur2 = node1, node2
    while cur1 and cur2:
        if cur1.data != cur2.data:
            return False
        cur1, cur2 = cur1.next, cur2.next
    return cur1 is None and cur2 is None
