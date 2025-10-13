from typing import List, TypeVar
T = TypeVar("T")


def rotate_matrix_inplace(matrix: List[List[T]]) -> List[List[T]]:
    """
    Rotates a matrix 90 degrees in a clockwise direction.
    Supports only square matrices.

    Args:
        matrix (List[List[T]]): The matrix to be rotated.

    Returns:
        List[List[T]]: The same matrix, modified in place.

    Analysis:
        Time complexity: O(N^2)
        Space complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return []

    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be a square.")

    N = len(matrix)

    for layer in range(N // 2):
        first = layer
        last = N - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last-offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

    return matrix
