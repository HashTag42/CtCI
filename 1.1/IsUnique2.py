'''
Cracking the Coding Interview - Problem 1.1
    Is Unique: Implement an algorithm to determine if a string has all unique characters.
        What if you cannot use additional data structures?
'''


def IsUnique(s: str) -> bool:
    """
    Checks if a string has all unique characters.

    Args:
        s (str) : The string to check.

    Returns:
        bool: True if the string has all unique characters. False otherwise.
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                return False
    return True
