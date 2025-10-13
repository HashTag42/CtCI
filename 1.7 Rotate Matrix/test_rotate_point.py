from rotate_point import rotate_point
import pytest


@pytest.fixture(params=[
    #
    # 1x1 matrix
    # [[1]] => [[1]]
    #
    (1, 1, 0, 0, (0, 0)),
    #
    # 3x3 matrix
    # [[1, 2, 3]    =>  [[7, 4, 1]
    #  [4, 5, 6]    =>   [8, 5, 2]
    #  [7, 8, 9]]   =>   [9, 6, 3]]
    #
    (3, 3, 0, 0, (2, 0)),   # 1
    (3, 3, 1, 0, (2, 1)),   # 2
    (3, 3, 2, 0, (2, 2)),   # 2
    (3, 3, 0, 1, (1, 0)),   # 4
    (3, 3, 1, 1, (1, 1)),   # 5
    (3, 3, 2, 1, (1, 2)),   # 6
    (3, 3, 0, 2, (0, 0)),   # 7
    (3, 3, 1, 2, (0, 1)),   # 8
    (3, 3, 2, 2, (0, 2)),   # 9
    #
    # 3x5 matrix
    # [[A, B, C]
    #  [D, E, F]    =>  [[M, J, G, D, A]
    #  [G, H, I]    =>   [N, K, H, E, B]
    #  [J, K, L]    =>   [O, L, I, F, C]]
    #  [M, N, O]]
    #
    (3, 5, 0, 0, (4, 0)),    # A
    (3, 5, 2, 0, (4, 2)),    # C
    (3, 5, 1, 2, (2, 1)),    # H
    (3, 5, 0, 4, (0, 0)),    # M
    (3, 5, 2, 4, (0, 2)),    # O
    #
    # 5x3 matrix
    #                       [[K, F, A]
    # [[A, B, C, D, E]  =>   [L, G, B]
    #  [F, G, H, I, J]  =>   [M, H, C]
    #  [K, L, M, N, O]] =>   [N, I, D]
    #                        [O, J, E]]
    #
    (5, 3, 0, 0, (2, 0)),    # A
    (5, 3, 4, 0, (2, 4)),    # E
    (5, 3, 2, 1, (1, 2)),    # H
    (5, 3, 0, 2, (0, 0)),    # K
    (5, 3, 4, 2, (0, 4)),    # O
    #
    # 7x7 matrix
    #
    (7, 7, 2, 1, (5, 2)),
    (7, 7, 4, 1, (5, 4)),
    (7, 7, 2, 3, (3, 2)),
    (7, 7, 4, 3, (3, 4)),
    (7, 7, 2, 5, (1, 2)),
])
def test_case(request: pytest.FixtureRequest):
    return request.param


def test_rotate_point(test_case):
    W, H, x, y, expected = test_case
    assert expected == rotate_point(W, H, x, y)


@pytest.fixture(params=[
    (3, 3, 3, 0),
    (3, 3, 0, 3),
])
def test_exception(request: pytest.FixtureRequest):
    return request.param


def test_rotate_point_ValueError(test_exception):
    with pytest.raises(ValueError):
        W, H, x, y = test_exception
        rotate_point(W, H, x, y)
