'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth element of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
from LinkedList import LinkedList, Node


def intersection(ll1: LinkedList, ll2: LinkedList) -> Node:
    l1, l2 = ll1.to_list(), ll2.to_list()
    for i1 in range(len(l1)):
        for i2 in range(len(l2)):
            if l1[i1:] == l2[i2:]:
                return l1[i1]
    return None
