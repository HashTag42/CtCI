'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth element of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
from LinkedList import LinkedList, Node


def intersection(ll1: LinkedList, ll2: LinkedList) -> Node:
    for n1 in ll1:
        for n2 in ll2:
            if n1 == n2:
                return n1
    return None
