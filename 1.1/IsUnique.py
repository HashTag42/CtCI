'''
Cracking the Coding Interview - Problem 1.1
    Is Unique: Implement an algorithm to determine if a string has all unique characters.
        What if you cannot use additional data structures?
'''


def IsUnique1(s: str) -> bool:
    """
    Checks if a string has all unique characters.

    Args:
        s (str) : The string to check.

    Returns:
        bool: True if the string has all unique characters. False otherwise.

    Description:
        Implementation uses a dictionary to track which characters have been found as we scan the string.
        Time complexity: O(N)
        Space complexity: O(N)
    """
    instances = {}
    for c in s:
        value = instances.get(c)
        if value is None:
            instances[c] = 1
        else:
            return False
    return True


def IsUnique2(s: str) -> bool:
    """
    Checks if a string has all unique characters.

    Args:
        s (str) : The string to check.

    Returns:
        bool: True if the string has all unique characters. False otherwise.

    Description:
        Implementation does not use any additional data structures. It scans the string twice to find duplicates.
        Time complexity: O(N^2)
        Space complexity: O(1)
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                return False
    return True
