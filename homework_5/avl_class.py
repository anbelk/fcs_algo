from avl_node import AVLNode

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is not None:
            return node.height
        else:
            return 0

    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _get_height_difference(self, node):
        if node is not None:
            return self._height(node.left) - self._height(node.right)
        else:
            return 0
        
    def is_balanced(self):
        return self._is_balanced_rec(self.root)[0]

    def _is_balanced_rec(self, node):
        if node is None:
            return True, 0

        left_balanced, left_height = self._is_balanced_rec(node.left)
        right_balanced, right_height = self._is_balanced_rec(node.right)

        height = 1 + max(left_height, right_height)
        height_diff = abs(left_height - right_height)

        if left_balanced and right_balanced and height_diff <= 1:
            return True, height
        else:
            return False, height

    def _right_rotate(self, A):
        B = A.left
        E = B.right
        B.right = A
        A.left = E
        self._update_height(A)
        self._update_height(B)
        return B

    def _left_rotate(self, A):
        C = A.right
        F = C.left
        C.left = A
        A.right = F
        self._update_height(A)
        self._update_height(C)
        return C

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        else:
            return node

        self._update_height(node)
        height_diff = self._get_height_difference(node)

        if height_diff > 1 and key < node.left.key:
            return self._right_rotate(node)

        if height_diff < -1 and key > node.right.key:
            return self._left_rotate(node)

        if height_diff > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if height_diff < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            nearest_node = self._get_min_node(node.right)
            node.key = nearest_node.key
            node.right = self._delete_rec(node.right, nearest_node.key)

        self._update_height(node)
        height_diff = self._get_height_difference(node)

        if height_diff > 1 and key < node.left.key:
            return self._right_rotate(node)

        if height_diff < -1 and key > node.right.key:
            return self._left_rotate(node)

        if height_diff > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if height_diff < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def inorder(self):
        keys = []
        self._inorder_rec(self.root, keys)
        return keys

    def _inorder_rec(self, node, keys):
        if node is not None:
            self._inorder_rec(node.left, keys)
            keys.append(node.key)
            self._inorder_rec(node.right, keys)