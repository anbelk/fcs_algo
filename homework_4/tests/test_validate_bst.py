import pytest
from bst_node import BSTNode

def is_valid_bst(root):
    keys = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        keys.append(node.key)
        inorder(node.right)

    inorder(root)

    for i in range(1, len(keys)):
        if keys[i] <= keys[i - 1]:
            return False
    return True


class TestValidateBST:
    @pytest.mark.parametrize("tree, expected", [
        (None, True),
        (BSTNode(5), True),
        (BSTNode(5, BSTNode(3), BSTNode(7)), True),
        (BSTNode(5, BSTNode(3), BSTNode(4)), False),
        (BSTNode(5, BSTNode(6), BSTNode(7)), False),
        (BSTNode(5,
                 BSTNode(3, BSTNode(2), BSTNode(4)),
                 BSTNode(8, BSTNode(7), BSTNode(9))),
         True),
        (BSTNode(5,
                 BSTNode(3, BSTNode(2), BSTNode(6)),
                 BSTNode(8)),
         False),
        (BSTNode(5,
                 BSTNode(2),
                 BSTNode(8, BSTNode(7), BSTNode(4))),
         False),
        (BSTNode(5, BSTNode(3), BSTNode(5)), False),
        (BSTNode(0,
                 BSTNode(-3, BSTNode(-5), BSTNode(-1)),
                 BSTNode(4, BSTNode(2), BSTNode(6))),
         True),
    ])
    def test_is_valid_bst(self, tree, expected):
        assert is_valid_bst(tree) == expected
