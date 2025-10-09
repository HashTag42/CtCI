from URLify import URLify
import pytest


@pytest.fixture(params=[
    ("", 0, ""),
    ("Mr John Smith      ", 13, "Mr%20John%20Smith"),
])
def test_case(request):
    return request.param


def test_URLify(test_case):
    string, true_length, expected = test_case
    actual = URLify(string, true_length)
    assert actual == expected
