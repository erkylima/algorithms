from collections import deque

from data_structure.tree.dfs_tree import BinarySearchTree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(root):
    if not root:
        return -1

    queue = deque([(root, 0)])
    max_height = 0
    while queue:
        node, height_level = queue.popleft()
        max_height = max(height_level, max_height)

        if node.left:
            queue.append((node.left, height_level+1))
        if node.right:
            queue.append((node.right, height_level+1))
        print(node.value)
    return max_height


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
print(height(root))