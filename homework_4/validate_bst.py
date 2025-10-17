from bst_node import BSTNode

def is_valid_bst(root: BSTNode) -> bool:
    keys = []

    def inorder(node: BSTNode):
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
