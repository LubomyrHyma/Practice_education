from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def is_full(node):
    if node is None:
        return True
    if (node.left is None) != (node.right is None):
        return False
    return is_full(node.left) and is_full(node.right)

def is_complete(root):
    if root is None:
        return True
    queue = deque([root])
    end = False
    while queue:
        current = queue.popleft()
        if current.left:
            if end:
                return False
            queue.append(current.left)
        else:
            end = True
        if current.right:
            if end:
                return False
            queue.append(current.right)
        else:
            end = True
    return True

def tree_depth(node):
    if node is None:
        return 0
    return 1 + max(tree_depth(node.left), tree_depth(node.right))

def is_perfect(root):
    def check(node, depth, level=0):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return depth == level + 1
        if node.left is None or node.right is None:
            return False
        return check(node.left, depth, level + 1) and check(node.right, depth, level + 1)

    depth = tree_depth(root)
    return check(root, depth)



def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')


block_values = [50.0, 30.0, 70.0, 20.0, 40.0, 60.0, 80.0]

root = None
for value in block_values:
    root = insert(root, value)

types = []
if is_complete(root):
    types.append("complete")
if is_full(root):
    types.append("full")
if is_perfect(root):
    types.append("perfect")

print("Tree type:", ", ".join(types))

print("\nPre-order traversal:")
preorder(root)

print("\n\nIn-order traversal:")
inorder(root)

print("\n\nPost-order traversal:")
postorder(root)
print() 