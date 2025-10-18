import pytest
from bst_node import BSTNode
from is_bst_valid import is_valid

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
    def test_is_bst_valid(self, tree, expected):
        assert is_valid(tree) == expected
