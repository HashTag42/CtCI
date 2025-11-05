'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.4 Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the “right partition”; it does not need
to appear between the left and right partitions. The additional spacing the example below indicates the partition.)

EXAMPLE
Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2       ->        10 -> 5 -> 5 -> 8"
'''
from typing import List
from LinkedList import LinkedList, Node


def partition_list(linked_list: List[int], partition) -> List[int]:
    ll = LinkedList(linked_list)
    list_right, list_left = list(), list()

    current = ll.head
    while current:
        if current.data < partition:
            list_left.append(current.data)
        else:
            list_right.append(current.data)
        current = current.next

    def append(linked_list: LinkedList, data: int) -> None:
        new_node = Node(data)
        if linked_list.head:
            current = linked_list.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            linked_list.head = new_node

    ll.head = None
    current = ll.head
    for val in list_left:
        append(ll, val)
    for val in list_right:
        append(ll, val)

    return ll
