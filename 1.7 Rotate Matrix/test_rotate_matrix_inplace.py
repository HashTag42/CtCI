from rotate_matrix_inplace import rotate_matrix_inplace
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


def test_rotate_matrix_inplace(test_case):
    input, expected = test_case
    assert expected == rotate_matrix_inplace(input)


@pytest.fixture(params=[
    # 3x5 matrix
    ([[1,  2,  3],
      [4,  5,  6],
      [7,  8,  9],
      [10, 11, 12],
      [13, 14, 15]]),
])
def test_ValueError(request: pytest.FixtureRequest):
    return request.param


def test_rotate_matrix_inplace_ValueError(test_ValueError):
    with pytest.raises(ValueError):
        matrix = test_ValueError
        rotate_matrix_inplace(matrix)
