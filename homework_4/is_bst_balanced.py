from bst_node import BSTNode

def is_balanced(root: BSTNode) -> bool:
    if root is None:
        return True

    stack = [(root, False)]
    heights = {}

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            if abs(left_height - right_height) > 1:
                return False
            heights[node] = 1 + max(left_height, right_height)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return True
