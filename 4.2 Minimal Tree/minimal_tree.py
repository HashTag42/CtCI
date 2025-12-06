'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 4.2 Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree
with minimal height.
'''
from typing import Optional


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None

    def _display(self, nesting=0) -> str:
        indent = " " * nesting * 2
        output = f"{self.value}\n"
        if self.left is not None and self.left.value is not None:
            output += f"{indent}L:"
            output += self.left._display(nesting + 1)
        if self.right is not None and self.right.value is not None:
            output += f"{indent}R:"
            output += self.right._display(nesting + 1)
        return output

    def __repr__(self) -> str:
        return self._display()


def create_minimal_tree(nodes: list[int]) -> BinaryTreeNode:
    return _create_minimal_bst(nodes, 0, len(nodes) - 1)


def _create_minimal_bst(nodes: list[int], start: int, end: int) -> BinaryTreeNode:
    if end < start:
        return BinaryTreeNode(None)
    mid: int = (start + end) // 2
    n = BinaryTreeNode(nodes[mid])
    n.left = _create_minimal_bst(nodes, start, mid - 1)
    n.right = _create_minimal_bst(nodes, mid + 1, end)
    return n


# if __name__ == "__main__":
#     # import pytest
#     # import sys
#     # sys.exit(pytest.main(['-v', "./4.2 Minimal Tree/minimal_tree_test.py"]))

#     test_cases = [
#         # nodes
#         ([0, 1, 2]),
#         ([0, 1, 2, 3]),
#         ([0, 1, 2, 3, 4]),
#         ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]),
#     ]

#     for tc in test_cases:
#         print(str(create_minimal_tree(tc)))
