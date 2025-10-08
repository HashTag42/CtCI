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


def IsPalindromePermutation(string: str) -> bool:
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
    """
    # Count the number of instances of each character in the string. Ignore spaces.
    character_dict = {}
    for c in string:
        cl = c.lower()
        if cl.isalpha():
            if cl in character_dict:
                character_dict[cl] += 1
            else:
                character_dict[cl] = 1

    # Check if the number of instances of each character is an even number.
    # Only one character is allowed to have an odd number of instances.
    has_odd = False
    for i in character_dict:
        if character_dict[i] % 2 != 0:
            if has_odd:
                return False
            else:
                has_odd = True
    return True
