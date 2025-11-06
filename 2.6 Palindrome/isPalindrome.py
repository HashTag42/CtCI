'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 2.6 Palindrome

Implement a function to check if a linked list is a palindrome.
'''
from LinkedList import LinkedList


def isPalindrome(linked_list: LinkedList) -> bool:
    vals = linked_list.to_list()
    if vals == vals[::-1]:
        return True
    else:
        return False
