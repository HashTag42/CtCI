from zero_matrix import zero_matrix
import pytest


@pytest.fixture(params=[
    # Empty matrix
    ([], []),
    # 1x1 matrix
    ([[0]], [[0]]),
    # 1x1 matrix
    ([[1]], [[1]]),
    # 3x3 matrix
    ([[1, 2, 3],
      [4, 0, 6],
      [7, 8, 9]],
     [[1, 0, 3],
      [0, 0, 0],
      [7, 0, 9]]),
    # 3x5 matrix
    ([[1,  2,  3],
      [0,  5,  6],
      [7,  8,  9],
      [10, 11, 0],
      [13, 14, 15]],
     [[0,  2,  0],
      [0,  0,  0],
      [0,  8,  0],
      [0,  0,  0],
      [0, 14, 0]]),
    # 7x7 matrix
    ([[0, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1],
      [1, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1],
      [1, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 0]],
     [[0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0]]),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_zero_matrix(test_case):
    matrix, expected = test_case
    assert expected == zero_matrix(matrix)
