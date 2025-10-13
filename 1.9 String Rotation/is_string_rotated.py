'''
    Cracking the Coding Interview - 6th Edition
    Question 1.9: String Rotation
    Assume you have a method isSubstring which checks if one word is a substring of another.
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
    to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat").
'''


def is_string_rotated(s1: str, s2: str) -> bool:
    """
    Checks if string s2 is a rotated version of string s1.

    Args:
        s1 (str): the original string to check against
        s2 (str): the potentially rotated version of s1

    Returns:
        bool: True if s2 is a rotated version of s1. False otherwise.
    """
    if len(s1) != len(s2):
        return False

    return is_substring(s2, s1 + s1)


def is_substring(substring: str, string: str) -> bool:
    return substring in string
