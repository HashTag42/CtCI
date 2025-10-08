'''
Cracking the Coding Interview - Problem 1.2
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
'''


def CheckPermutation(s1: str, s2: str) -> bool:
    """
    Checks if one string is a permutation of another.

    Args:
        s1 (str) : The first string to check.
        s1 (str) : The second string to check against.

    Returns:
        bool : True if one string is a permutation of the other. False otherwise.

    Description:
        Uses two dictionaries to track character instances and then compares those dictionaries.
        Time complexity: O(N)
        Space complexity: O(N)
    """
    if len(s1) != len(s2):
        return False
    s1dict, s2dict = {}, {}
    for c in s1:
        if c in s1dict:
            s1dict[c] += 1
        else:
            s1dict[c] = 1
    for c in s2:
        if c in s2dict:
            s2dict[c] += 1
        else:
            s2dict[c] = 1
    if s1dict == s2dict:
        return True
    else:
        return False
