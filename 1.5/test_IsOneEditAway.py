from IsOneEditAway import IsOneEditAway
import pytest


@pytest.fixture(params=[
    # returns True
    ("", "", True),             # Identical empty strings
    ("pale", "pale", True),     # Identical strings
    ("pale", "ale", True),      # 1 edit, 1 removal, 1st character
    ("pale", "ple", True),      # 1 edit, 1 removal, 2nd character
    ("pale", "pal", True),      # 1 edit, 1 removal, last character
    ("pale", "zpale", True),    # 1 edit, 1 insertion, 1st character
    ("pale", "pzale", True),    # 1 edit, 1 insertion, 2nd character
    ("pale", "palez", True),    # 1 edit, 1 insertion, last character
    ("pale", "zale", True),     # 1 edit, 1 replacement, 1st character
    ("pale", "pzle", True),     # 1 edit, 1 replacement, 2nd character
    ("pale", "palz", True),     # 1 edit, 1 replacement, last character
    # returns False
    ("pale", "zzke", False),    # 2 edits, 2 replacements, first 2 characters
    ("pale", "pzze", False),    # 2 edits, 2 replacements, middle characters
    ("pale", "pazz", False),    # 2 edits, 2 replacements, last 2 characters
    ("aa", "aaaa", False),      # String lengths diff = 2, 1st string is shorter
    ("aaaa", "aa", False),      # String lengths diff = 2, 2nd string is shorter
    ("", "aaa", False),         # String length diff > 2
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_IsOneEditAway(test_case):
    input_string1, input_string2, expected = test_case
    actual = IsOneEditAway(input_string1, input_string2)
    assert actual == expected
