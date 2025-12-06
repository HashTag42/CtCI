from minimal_tree import create_minimal_tree, BinaryTreeNode
import pytest

test_cases = [
    # nodes
    ([0, 1, 2]),
    ([0, 1, 2, 3]),
    ([0, 1, 2, 3, 4]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]),
]


@pytest.mark.parametrize("nodes", test_cases)
def test_create_minimal_tree(nodes):
    root: BinaryTreeNode = create_minimal_tree(nodes)
    print(str(root))


def test_BinaryTreeNode__display():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(0)
    root.right = BinaryTreeNode(2)
    print(str(root))
