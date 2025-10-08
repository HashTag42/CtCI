from IsUnique import IsUnique1
from IsUnique import IsUnique2
import pytest


@pytest.fixture(params=[
        ("ab", True),
        ("aa", False),
        ("", True),
        ("abcdef0123456ABCDEFáñ☺️東京", True),
])
def test_case(request):
    return request.param


def test_IsUnique1(test_case):
    input_str, expected = test_case
    actual = IsUnique1(input_str)
    assert actual == expected


def test_IsUnique2(test_case):
    input_str, expected = test_case
    actual = IsUnique2(input_str)
    assert actual == expected
