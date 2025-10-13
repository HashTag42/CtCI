from is_string_rotated import is_string_rotated
import pytest


@pytest.fixture(params=[
    # returns True
    ("", "", True),
    ("a", "a", True),
    ("waterbottle", "waterbottle", True),
    ("waterbottle", "erbottlewat", True),
    ("apple", "pleap", True),
    ("hello", "llohe", True),
    ("abc", "cab", True),
    # returns False
    ("abc", "abcd", False),         # different lengths
    ("camera", "macera", False),
    ("foo", "bar", False),
    ("foo", "foofoo", False),
    ("hello", "helol", False),
    ("abc", "acb", False),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_is_string_rotated(test_case):
    s1, s2, expected = test_case
    assert expected == is_string_rotated(s1, s2)
