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
    """Return the node at the start of the loop if one exists, else None.
    Uses Floyd's cycle detection algorithm (O(1) space).
    Complexity: Time: O(n), Space: O(1)"""
    slow = fast = head
    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    # Step 2: Find start of loop
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow
