'''
    Cracking the Coding Interview - 6th Edition
    Question 2.1 - Return Kth to Last
    Implement an algorithm to find the kth to last element of a single linked list.
'''
from LinkedList import LinkedList


def return_Kth_to_last(linked_list: LinkedList, Kth: int) -> int:
    """
    Time complexity: O(2*n) = O(n)
    Space complexity: O(1)
    """
    list_len = len(linked_list)
    if list_len == 0:
        raise ValueError("List must have at least 1 element")

    if Kth < 0 or list_len <= Kth:
        raise ValueError("Kth must be within the list boundaries")

    target = list_len - Kth - 1

    count = 0
    current = linked_list.head
    while current:
        if count == target:
            return current.data
        count += 1
        current = current.next
