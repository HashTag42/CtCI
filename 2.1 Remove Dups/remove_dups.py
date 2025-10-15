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

        Args:
            linked_list (list): the source LinkedList

        Returns:
            (list): a new LinkedList with the duplicates removed
    """
    ll, ll2 = LinkedList(), LinkedList()
    ll.append_from_list(linked_list)
    s = set()
    for val in ll:
        if val not in s:
            s.add(val)
            ll2.append(val)
    return ll2.to_list()


def remove_dups2(linked_list: List[int]) -> List[int]:
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
