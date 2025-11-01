'''
    Cracking the Coding Interview - 6th Edition
    Question 2.3 Delete Middle Node
    Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node) of a singly linked
     list, given access only to that node.
    EXAMPLE
    Input: the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned but the new linked list looks like a->b->d->e->f
'''
from LinkedList import Node


def delete_middle_node(node: Node) -> None:
    previous = node
    current = node
    while current:
        previous.data = current.data
        if current.next is None:
            previous.next = None
            break
        previous = current
        current = current.next
