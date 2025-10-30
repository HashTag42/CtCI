'''
    Cracking the Coding Interview - 6th Edition
    Question 2.2 - Return Kth to Last
    Implement an algorithm to find the kth to last element of a single linked list.
'''
from LinkedList import LinkedList, Node
error_empty_list = "List must have at least 1 element"
error_list_boundaries = "Kth must be within the list boundaries"


def return_Kth_to_last1(linked_list: LinkedList, Kth: int) -> int:
    """
    Relies on the LinkedList class len() method.
    Time complexity: O(2*n) = O(n)
    Space complexity: O(1)
    """
    list_len = len(linked_list)
    if list_len == 0:
        raise ValueError(error_empty_list)
    if Kth < 0 or list_len <= Kth:
        raise ValueError(error_list_boundaries)

    target = list_len - Kth - 1

    count = 0
    current = linked_list.head
    while current:
        if count == target:
            return current.data
        count += 1
        current = current.next


def return_Kth_to_last2(head: Node, Kth: int) -> int:
    """
    Does not rely on the LinkedList class.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    items = list()
    list_len = 0
    current = head
    while current:
        items.append(current.data)
        list_len += 1
        current = current.next

    if list_len == 0:
        raise ValueError(error_empty_list)
    if Kth < 0 or list_len <= Kth:
        raise ValueError(error_list_boundaries)

    return items[list_len - Kth - 1]


def return_Kth_to_last3(head: Node, Kth: int) -> int:
    """
    Two-pointer solution
    Time complexity: O(n)
    Space complexity: O(1)
    """
    p1 = head
    for i in range(Kth + 1):
        if p1 is None:
            raise ValueError(error_list_boundaries)
        p1 = p1.next

    p2 = head
    while p1:
        p1 = p1.next
        p2 = p2.next

    if p2 is None:
        raise ValueError(error_empty_list)

    return p2.data
