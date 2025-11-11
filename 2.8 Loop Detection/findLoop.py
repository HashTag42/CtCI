'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.8 Loop Detection

Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked listL A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a
loop in the linked list.
EXAMPLE
Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
'''
from typing import Optional
from LinkedList import Node


def findLoop(head: Optional[Node]) -> Optional[Node]:
    """Return the node at the start of the loop if one exists, else None."""
    """Complexity: Time: O(n), Space: O(n)"""
    nodes = set()
    current = head
    while current:
        if current in nodes:
            return current
        nodes.add(current)
        current = current.next
    return None
