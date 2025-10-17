import pytest
from bst_class import BST

class TestBSTInsert:
    def test_insert_one(self):
        bst = BST()
        bst.insert(10)
        assert bst.root is not None
        assert bst.root.key == 10
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_left_and_right(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.root.key == 10
        assert bst.root.left.key == 5
        assert bst.root.right.key == 15
        assert bst.root.left.parent == bst.root
        assert bst.root.right.parent == bst.root

    def test_insert_complex(self):
        bst = BST()
        values = [10, 5, 15, 3, 7, 12, 18]
        for v in values:
            bst.insert(v)
        assert bst.root.left.left.key == 3
        assert bst.root.left.right.key == 7
        assert bst.root.right.left.key == 12
        assert bst.root.right.right.key == 18

class TestBSTPreorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [5, 3, 7]),
        ([5, 3, 7, 2, 4, 6, 8], [5, 3, 2, 4, 7, 6, 8]),
        ([10, 5, 15, 3, 7, 12, 18], [10, 5, 3, 7, 15, 12, 18]),
        ([5, 3, 5, 2], [5, 3, 2, 5]),
    ])
    def test_preorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.preorder() == expected


class TestBSTPostorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [3, 7, 5]),
        ([5, 3, 7, 2, 4, 6, 8], [2, 4, 3, 6, 8, 7, 5]),
        ([10, 5, 15, 3, 7, 12, 18], [3, 7, 5, 12, 18, 15, 10]),
        ([5, 3, 5, 2], [2, 3, 5, 5]),
    ])
    def test_postorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.postorder() == expected


class TestBSTInorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [3, 5, 7]),
        ([5, 3, 7, 2, 4, 6, 8], [2, 3, 4, 5, 6, 7, 8]),
        ([10, 5, 15, 3, 7, 12, 18], [3, 5, 7, 10, 12, 15, 18]),
        ([5, 3, 5, 2], [2, 3, 5, 5]),
    ])
    def test_inorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.inorder() == expected


class TestBSTReversePreorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [5, 7, 3]),
        ([5, 3, 7, 2, 4, 6, 8], [5, 7, 8, 6, 3, 4, 2]),
        ([10, 5, 15, 3, 7, 12, 18], [10, 15, 18, 12, 5, 7, 3]),
        ([5, 3, 5, 2], [5, 5, 3, 2]),
    ])
    def test_reverse_preorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.reverse_preorder() == expected


class TestBSTReversePostorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [7, 3, 5]),
        ([5, 3, 7, 2, 4, 6, 8], [8, 6, 7, 4, 2, 3, 5]),
        ([10, 5, 15, 3, 7, 12, 18], [18, 12, 15, 7, 3, 5, 10]),
        ([5, 3, 5, 2], [5, 2, 3, 5]),
    ])
    def test_reverse_postorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.reverse_postorder() == expected


class TestBSTReverseInorder:
    @pytest.mark.parametrize("values, expected", [
        ([], []),
        ([5], [5]),
        ([5, 3, 7], [7, 5, 3]),
        ([5, 3, 7, 2, 4, 6, 8], [8, 7, 6, 5, 4, 3, 2]),
        ([10, 5, 15, 3, 7, 12, 18], [18, 15, 12, 10, 7, 5, 3]),
        ([5, 3, 5, 2], [5, 5, 3, 2]),
    ])
    def test_reverse_inorder(self, values, expected):
        bst = BST()
        for v in values:
            bst.insert(v)
        assert bst.reverse_inorder() == expected