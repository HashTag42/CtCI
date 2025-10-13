from typing import List, TypeVar
from rotate_point import rotate_point
T = TypeVar("T")


def rotate_matrix(matrix: List[List[T]]) -> List[List[T]]:
    """
    Rotates a matrix 90 degrees in a clockwise direction.
    This supports matrices of any dimensions.

    Args:
        matrix (List[List[T]]): The matrix to be rotated.

    Returns:
        List[List[T]]: The rotated matrix.

    Analysis:
        Time complexity: O(rows x cols)
        Space complexity: O(rows x cols)
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    rotated_matrix = [[None for _ in range(rows)] for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            new_col, new_row = rotate_point(cols, rows, col, row)
            rotated_matrix[new_row][new_col] = matrix[row][col]

    return rotated_matrix
