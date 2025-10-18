import pytest
from bst_node import BSTNode
from is_bst_balanced import is_balanced

class TestBalancedBST:
    @pytest.mark.parametrize("tree, expected", [
        (None, True),
        (BSTNode(1), True),
        (BSTNode(1, BSTNode(2), BSTNode(3)), True),
        (BSTNode(1, BSTNode(2, BSTNode(3), None), None), False),
        (BSTNode(1, None, BSTNode(2, None, BSTNode(3))), False),
        (BSTNode(1,
                 BSTNode(2, BSTNode(4), BSTNode(5)),
                 BSTNode(3, BSTNode(6), BSTNode(7))),
         True),
        (BSTNode(1,
                 BSTNode(2, BSTNode(3, BSTNode(4), None), None),
                 BSTNode(5)),
         False),
        (BSTNode(0,
                 BSTNode(-3, BSTNode(-5), BSTNode(-1)),
                 BSTNode(4, BSTNode(2), BSTNode(6))),
         True),
    ])
    def test_is_bst_balanced(self, tree, expected):
        assert is_balanced(tree) == expected