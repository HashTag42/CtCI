from remove_dups import remove_dups1, remove_dups2
import pytest


@pytest.fixture(params=[
    ([], []),                                           # Empty list
    ([1], [1]),                                         # One item, no dup
    ([1, 1], [1]),                                      # One dup
    ([1, 2, 3, 2], [1, 3, 2]),                          # One dup
    ([1, 2, 3, 1, 4, 1], [2, 3, 4, 1]),                 # Two dups
    (["A", "B", "C", "D"], ["A", "B", "C", "D"]),       # No dups
])
def test_case1(request: pytest.FixtureRequest):
    return request.param


def test_remove_dups1(test_case1):
    input, expected = test_case1
    assert expected == remove_dups1(input)


@pytest.fixture(params=[
    ([], []),                                           # Empty list
    ([1], [1]),                                         # One item, no dup
    ([1, 1], [1]),                                      # One dup
    ([1, 2, 3, 2], [1, 2, 3]),                          # One dup
    ([1, 2, 3, 1, 4, 1], [1, 2, 3, 4]),                 # Two dups
    (["A", "B", "C", "D"], ["A", "B", "C", "D"]),       # No dups
])
def test_case2(request: pytest.FixtureRequest):
    return request.param


def test_remove_dups2(test_case2):
    input, expected = test_case2
    assert expected == remove_dups2(input)
