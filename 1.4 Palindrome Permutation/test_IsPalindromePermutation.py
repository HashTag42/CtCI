from IsPalindromePermutation import IsPalindromePermutation
import pytest


@pytest.fixture(params=[
    # positive cases
    ("", True),                                 # empty string is trivially valid
    (" ", True),
    ("a", True),
    ("azAZ", True),
    ("Rats live on no evil star", True),        # full palindrome
    ("A man, a plan, a canal, panama", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),        # case-insensitive palindrome
    ("no x in nixon", True),
    ("☺️👍🏽👍🏽⚾⚾", True),                      # unicode characters
    ("Tact Coa", True),                         # classic example
    ("A man, a plan, a canal, Panama", True),   # normalized palindrome
    ("a", True),                                # single character
    ("aa", True),                               # even count
    ("aabbccdde", True),                        # one odd count
    ("aabbccdd", True),                         # all even
    ("123 taco cat!", True),                    # digits/punctuation ignored
    ("Was it a car or a cat I saw?", True),     # palindrome with punctuation
    ("No lemon, no melon", True),               # palindrome phrase
    # negative cases
    ("So patient a nurse to nurse a patient so", False),
    ("Not a palindrome", False),            # clearly not
    ("abc", False),                         # three odd counts
])
def test_case(request):
    return request.param


def test_IsPalindromePermutation(test_case):
    input_string, expected = test_case
    actual = IsPalindromePermutation(input_string)
    assert actual == expected
