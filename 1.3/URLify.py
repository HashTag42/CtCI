'''
Cracking the Coding Interview - Problem 1.3
    URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has
    sufficient space at the end to hold the additional characters, and that you're given the "true" length
    of the string.

    EXAMPLE
        Input: "Mr John Smith      ", 13
        Output: "Mr%20John%20Smith"
'''


def URLify(string: str, true_length: int) -> str:
    """
    Replaces spaces in a string with its URL-encoded representation: %20

    Args:
        string (str) : The source string containing spaces
        true_length (int): The "true" length of the string.

    Returns:
        str : The resulting string.
    """
    result = ""
    for i in range(true_length):
        if string[i] == ' ':
            result += "%20"
        else:
            result += string[i]
    return result
