'''
Cracking the Coding Interview, 6th edition
Question 1.5: One Away
There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Give two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLES
pale, ple   -> True
pales, pale -> True
pale, bale  -> True
pale, bake  -> False
'''


def IsOneEditAway(string1: str, string2: str) -> bool:

    if string1 == string2:
        return True

    if abs(len(string1) - len(string2)) >= 2:
        return False

    if len(string1) - len(string2) == 1:
        # Potential removal
        return CheckRemoval(string1, string2)

    if len(string1) - len(string2) == -1:
        # Potential insertion
        # An insertion is a reversed removal, so we pass the strings to CheckRemoval in reversed order
        return CheckRemoval(string2, string1)

    # len(string1) is == len(string2)
    # Potential replacement
    return CheckReplacement(string1, string2)


def CheckReplacement(string1: str, string2: str) -> bool:
    diff_count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff_count += 1

    if diff_count <= 1:
        return True
    else:
        return False


def CheckRemoval(string1: str, string2: str) -> bool:
    min_len = min(len(string1), len(string2))

    for i in range(min_len):
        if string1[i] != string2[i]:
            if string1[i+1:] == string2[i:]:
                return True
            else:
                return False

    return True
