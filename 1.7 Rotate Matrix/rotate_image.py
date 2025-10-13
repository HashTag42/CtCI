'''
Cracking the Coding Interview, 6th edition
Question 1.7: Rotate Matrix
Given an image represented by an NxN matrix, where each pixel is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

ASSUMPTION:
- The image is rotated in a clockwise direction.
'''

from typing import List, NamedTuple
from rotate_matrix import rotate_matrix


class Pixel(NamedTuple):
    r: int
    g: int
    b: int
    a: int


def rotate_image(image: List[List[Pixel]]) -> List[List[Pixel]]:
    """
    Rotates an image represented as a matrix of 4-byte pixels 90 degrees clockwise.

    Args:
        image (List[List[Pixel]]): NxN matrix of pixels.

    Returns:
        List[List[Pixel]]: Rotated image matrix.
    """
    return rotate_matrix(image)
