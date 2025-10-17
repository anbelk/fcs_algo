from bst_node import BSTNode

class BST():
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key=key)
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = BSTNode(key=key, parent=current_node)
                        break
                    else:
                        current_node = current_node.left
                elif key >= current_node.key:
                    if current_node.right is None:
                        current_node.right = BSTNode(key=key, parent=current_node)
                        break
                    else:
                        current_node = current_node.right

    def __isempty__(self):
        return True if self.root is None else False

    def preorder(self):
        keys = []
        if not self.__isempty__():
            stack = [self.root]
            while stack:
                node = stack.pop()
                keys.append(node.key)
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        return keys

    def reverse_preorder(self):
        keys = []
        if not self.__isempty__():
            stack = [self.root]
            while stack:
                node = stack.pop()
                keys.append(node.key)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return keys

    def inorder(self):
        keys = []
        if not self.__isempty__():
            stack = [(self.root, False)]
            while stack:
                node, visited = stack.pop()
                if node is None:
                    continue
                if visited:
                    keys.append(node.key)
                else:
                    if node.right is not None:
                        stack.append((node.right, False))
                    stack.append((node, True))
                    if node.left is not None:
                        stack.append((node.left, False))
        return keys

    def reverse_inorder(self):
        keys = []
        if not self.__isempty__():
            stack = [(self.root, False)]
            while stack:
                node, visited = stack.pop()
                if node is None:
                    continue
                if visited:
                    keys.append(node.key)
                else:
                    if node.left is not None:
                        stack.append((node.left, False))
                    stack.append((node, True))
                    if node.right is not None:
                        stack.append((node.right, False))
        return keys

    def postorder(self):
        keys = []
        if not self.__isempty__():
            stack = [(self.root, False)]
            while stack:
                node, visited = stack.pop()
                if node is None:
                    continue
                if visited:
                    keys.append(node.key)
                else:
                    stack.append((node, True))
                    if node.right is not None:
                        stack.append((node.right, False))
                    if node.left is not None:
                        stack.append((node.left, False))
        return keys

    def reverse_postorder(self):
        keys = []
        if not self.__isempty__():
            stack = [(self.root, False)]
            while stack:
                node, visited = stack.pop()
                if node is None:
                    continue
                if visited:
                    keys.append(node.key)
                else:
                    stack.append((node, True))
                    if node.left is not None:
                        stack.append((node.left, False))
                    if node.right is not None:
                        stack.append((node.right, False))
        return keys
