from CheckPermutation import CheckPermutation1, CheckPermutation2
import pytest


@pytest.fixture(params=[
    ("", "", True),
    ("abc", "cba", True),
    ("apple", "papel", True),
    ("carrot", "tarroc", True),
    ("aaa", "bbb", False),
    ("abba", "abcba", False),
])
def test_case(request):
    return request.param


def test_CheckPermutation1(test_case):
    string1, string2, expected = test_case
    actual = CheckPermutation1(string1, string2)
    assert actual == expected


def test_CheckPermutation2(test_case):
    string1, string2, expected = test_case
    actual = CheckPermutation2(string1, string2)
    assert actual == expected
