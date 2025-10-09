from IsPalindromePermutation import IsPalindromePermutation1
import pytest


@pytest.fixture(params=[
    # positive cases
    ("", True),  # empty string is trivially a palindrome
    (" ", True),
    ("azAZ", True),
    ("jhsabckuj ahjsbckj", True),
    ("no x in nixon", True),
    ("☺️👍🏽👍🏽⚾⚾", True),
    ("Tact Coa", True),  # classic example
    ("Rats live on no evil star", True),  # full palindrome
    ("A man, a plan, a canal, Panama", True),  # normalized palindrome
    ("a", True),  # single character
    ("aa", True),  # even count
    ("aabbccdde", True),  # one odd count
    ("aabbccdd", True),  # all even
    ("123 taco cat!", True),  # digits and punctuation ignored
    ("Was it a car or a cat I saw?", True),  # palindrome with punctuation
    ("No lemon, no melon", True),  # palindrome phrase
    ("Able was I ere I saw Elba", True),  # case-insensitive palindrome
    ("😊a😊a😊", True),  # emoji + letters (if emojis are filtered out)
    # negative cases
    ("Not a palindrome", False),  # clearly not
    ("abc", False),  # two odd counts
    ("abcabcabc", False),  # three odd counts
])
def test_case(request):
    return request.param


def test_IsPalindromePermutation1(test_case):
    input_string, expected = test_case
    actual = IsPalindromePermutation1(input_string)
    assert actual == expected
