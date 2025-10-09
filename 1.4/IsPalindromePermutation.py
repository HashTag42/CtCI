'''
Cracking the Coding Interview - Question 1.4
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards.
    A permutation is a rearrangement of the letters.
    The palindrome does not need to be limited to just dictionary words.

    EXAMPLE
        Input: Tact Coa
        Output: True (permutations: "taco cat", "atco cta", etc.)
'''


from collections import Counter


def IsPalindromePermutation1(string: str) -> bool:
    """
    Checks if the given string is a permutation of a palindrome.

    Args:
        string (str) : The string to check.

    Returns:
        bool : True if the string is a permutation of a palindrome. False otherwise.

    Description:
        Only letters are considered for the check.
        The check is case insensitive.
        Digits, punctuation, and whitespace are ignored.

        Time complexity: O(n)
        Space complexity: O(n)
    """
    # Count the number of instances of each character in the string
    filtered = [char.lower() for char in string if char.isalpha()]
    char_counts = Counter(filtered)

    # Count how many characters have an odd number of instances in the string
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)

    # Only one character can have an odd number of instances
    return odd_count <= 1



def IsPalindromePermutation2(string: str) -> bool:
    """
    """
