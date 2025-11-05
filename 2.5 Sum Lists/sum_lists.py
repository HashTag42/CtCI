'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.5 Sum Lists

You have two numbers represented by a linked list, where each node contains singles digit. The digits are stored in
reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
'''
from LinkedList import LinkedList


def sum_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    return get_reversed_ll_from_val(get_val_from_reversed_ll(list1) +
                                    get_val_from_reversed_ll(list2))


def get_val_from_reversed_ll(linked_list: LinkedList) -> int:
    current = linked_list.head
    val = 0
    x = 0
    while current:
        val += current.data * (10 ** x)
        x += 1
        current = current.next
    return val


def get_reversed_ll_from_val(val: int) -> LinkedList:
    ll = LinkedList()
    str_val = str(val)[::-1]
    for c in str_val:
        ll.append(int(c))
    return ll
