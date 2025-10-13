from rotate_matrix import rotate_matrix
import pytest


@pytest.fixture(params=[
    # Empty matrix
    ([], []),
    # 1x1 matrix
    ([[1]], [[1]]),
    # 3x3 matrix
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]]),
    # 3x5 matrix
    ([[1,  2,  3],
      [4,  5,  6],
      [7,  8,  9],
      [10, 11, 12],
      [13, 14, 15]],
     [[13, 10,  7,  4,  1],
      [14, 11,  8,  5,  2],
      [15, 12,  9,  6,  3]]),
    # 7x7 matrix, "on" points form an 'F'
    ([[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],],
     [[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],]),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_rotate_matrix(test_case):
    input, expected = test_case
    assert expected == rotate_matrix(input)
