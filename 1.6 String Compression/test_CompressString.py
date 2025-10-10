from CompressString import CompressString
import pytest


@pytest.fixture(params=[
    ("", ""),
    ("a", "a"),
    ("aa", "a2"),
    ("ab", "ab"),
    ("aabb", "a2b2"),
    ('abcdef', 'abcdef'),
    ("aabcccccaaa", "a2b1c5a3"),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_CompressString(test_case):
    input_string, expected = test_case
    actual = CompressString(input_string)
    assert actual == expected
