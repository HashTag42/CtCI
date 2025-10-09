from IsPalindromePermutation import IsPalindromePermutation
import pytest


@pytest.fixture(params=[
    ("", True),
    (" ", True),
    ("a", True),
    ("azAZ", True),
    ("Tact Coa", True),
    ("Rats live on no evil star", True),
    ("A man, a plan, a canal, panama", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("no x in nixon", True),
    ("☺️👍🏽👍🏽⚾⚾", True),
    ("So patient a nurse to nurse a patient so", False),
    ("abc", False),
])
def test_case(request):
    return request.param


def test_IsPalindromePermutation(test_case):
    input_string, expected = test_case
    actual = IsPalindromePermutation(input_string)
    assert actual == expected
