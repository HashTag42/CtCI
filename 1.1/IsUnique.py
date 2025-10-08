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
    instances = {}
    for c in s:
        value = instances.get(c)
        if value is None:
            instances[c] = 1
        else:
            return False
    return True
