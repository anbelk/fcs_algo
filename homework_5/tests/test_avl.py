import pytest
from avl_class import AVLTree

def test_insert_single():
    tree = AVLTree()
    tree.insert(10)
    assert tree.root.key == 10
    assert tree.inorder() == [10]
    assert tree.is_balanced() is True

def test_insert_multiple():
    tree = AVLTree()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    assert tree.inorder() == [10, 20, 25, 30, 40, 50]

def test_insert_duplicate_key():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(10)
    assert tree.inorder() == [10]

def test_search_existing_key():
    tree = AVLTree()
    for key in [10, 20, 30]:
        tree.insert(key)
    assert tree.search(20) is True

def test_search_non_existing_key():
    tree = AVLTree()
    for key in [10, 20, 30]:
        tree.insert(key)
    assert tree.search(40) is False

def test_delete_leaf():
    tree = AVLTree()
    for key in [10, 5, 15]:
        tree.insert(key)
    tree.delete(5)
    assert tree.inorder() == [10, 15]

def test_delete_node_with_one_child():
    tree = AVLTree()
    for key in [10, 5, 15, 12]:
        tree.insert(key)
    tree.delete(15)
    assert tree.inorder() == [5, 10, 12]
    assert tree.is_balanced() is True

def test_delete_node_with_two_children():
    tree = AVLTree()
    for key in [10, 5, 15, 12, 20]:
        tree.insert(key)
    tree.delete(15)
    assert tree.inorder() == [5, 10, 12, 20]
    assert tree.is_balanced() is True

def test_delete_root_node():
    tree = AVLTree()
    for key in [10, 5, 15]:
        tree.insert(key)
    tree.delete(10)
    assert tree.is_balanced() is True
    assert 10 not in tree.inorder()

def test_delete_non_existing_key():
    tree = AVLTree()
    for key in [10, 20, 30]:
        tree.insert(key)
    before = tree.inorder()
    tree.delete(99)
    after = tree.inorder()
    assert before == after
    assert tree.is_balanced() is True

def test_balance_after_rotations():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    assert tree.root.key == 20
    assert tree.is_balanced() is True

def test_balance_complex():
    tree = AVLTree()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    tree.delete(50)
    tree.delete(25)
    tree.insert(35)
    assert tree.is_balanced() is True
    assert sorted(tree.inorder()) == tree.inorder()
