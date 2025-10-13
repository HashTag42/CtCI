from typing import Tuple


def rotate_point(width: int, height: int, col: int, row: int) -> Tuple[int, int]:
    """
    Rotates a point in a matrix 90 degrees in a clockwise direction

    Args:
        width (int):    number of columns in the matrix
        height (int):   number of rows in the matrix
        col (int):      horizontal coordinate
        row (int):      vertical coordinate

    Returns:
        Tuple[int, int]: Rotated (new_row, new_col) coordinates

    Analysis:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Note:
        Assumes rotation within a rectangular matrix of size (height × width).
    """
    # TODO: Extend this function to also work in an anti-clockwise direction

    if width < 0 or height < 0 or col < 0 or row < 0:
        raise ValueError("Invalid argument(s). All arguments must be greater than zero.")

    if col >= width or row >= height:
        raise ValueError(
            f"Invalid coordinates: col={col}, row={row} exceed matrix bounds (width={width}, height={height})"
        )

    return height - row - 1, col
