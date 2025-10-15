'''
    Cracking the Coding Interview - 6th Edition
    Question 2.1 - Remove Dups
    Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is now allowed?
'''
from typing import List
from LinkedList import LinkedList


def remove_dups1(linked_list: List[int]) -> List[int]:
    """
        Removes duplicated items from an unsorted linked list.
        Uses a set to track previously seen items.
        Updates the source list in place.

        Args:
            linked_list (list): a list representing the source LinkedList

        Returns:
            (list): a list representing a new LinkedList with the duplicates removed

    """
    ll = LinkedList()
    ll.append_from_list(linked_list)
    seen = set()
    current = ll.head
    while current:
        if current.data in seen:
            ll.delete(current.data)
        else:
            seen.add(current.data)
        current = current.next
    return ll.to_list()


def remove_dups2(linked_list: List[int]) -> List[int]:
    """
        Removes duplicated items from an unsorted linked list.
        Does not use a temporary buffer.
        Updates the source list in place.

        Args:
            linked_list (list): a list representing the source LinkedList

        Returns:
            (list): the original linked list with the duplicates removed
    """
    ll = LinkedList()
    ll.append_from_list(linked_list)
    p1 = ll.head
    while p1:
        prev = None
        p2 = p1
        while p2:
            if p2.data == p1.data:
                if prev:
                    prev.next = p2.next
                else:
                    p1.next = p2.next
            prev = p2
            p2 = p2.next
        p1 = p1.next
    return ll.to_list()
