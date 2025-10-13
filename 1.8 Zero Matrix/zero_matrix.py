'''
    Cracking the Coding Interview - 6th Edition
    Question 1.8 Zero Matrix
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.
'''


from typing import List


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
        Zeroes out rows and columns in a matrix for elements that are zero

        Args:
            matrix (List[List[int]]): The matrix to be processed

        Returns:
            List[List[int]]: The same matrix, modified in place

        Analysss:
            Time complexity: O(M x N)
            Space complexity: O(M x N) for row/col tracking

    """
    if not matrix or not matrix[0]:
        return []

    height = len(matrix)
    width = len(matrix[0])

    # Scan the matrix collecting the rows and columns to zero out
    zero_rows = set()
    zero_cols = set()
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    # Zero out the collected rows
    for row in zero_rows:
        for col in range(width):
            matrix[row][col] = 0

    # Zero out the collected columns
    for row in range(height):
        for col in zero_cols:
            matrix[row][col] = 0

    return matrix
