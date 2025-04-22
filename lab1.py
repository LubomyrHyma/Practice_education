import csv


def load_blocks(filename):
    blocks = {}
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            block_id = row['id']
            view = int(row['view'])
            blocks[block_id] = {'view': view, 'votes': 0, 'added': False}
    return blocks

def load_votes(filename):
    votes_received = {}
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            block_id = row['block_id']
            votes_received[block_id] = votes_received.get(block_id, 0) + 1
    return votes_received

def build_chain(blocks, votes_received):
    chain = []
    expected_view = 0  
    while True:
        added_something = False
        for block_id, block in blocks.items():
            if (not block['added'] and votes_received.get(block_id, 0) > 0 and 
                block['view'] == expected_view):
                chain.append(block_id)
                block['added'] = True
                block['votes'] = votes_received.get(block_id, 0)
                expected_view += 1
                added_something = True
        if not added_something:  
            break
    return chain

def save_results(blocks, chain, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'view', 'votes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for block_id in chain:
            writer.writerow({'id': block_id, 'view': blocks[block_id]['view'], 'votes': blocks[block_id]['votes']})

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
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def build_bst(blocks):
    root = None
    for block in blocks:
        if 'votes' in block:
            root = insert(root, block['votes'])
    return root

def is_complete(root, index, num_nodes):
    if root is None:
        return True
    if index >= num_nodes:
        return False
    return is_complete(root.left, 2 * index + 1, num_nodes) and \
           is_complete(root.right, 2 * index + 2, num_nodes)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_full(root):
    if root is None:
        return True
    if (root.left is None and root.right is not None) or \
       (root.left is not None and root.right is None):
        return False
    return is_full(root.left) and is_full(root.right)

def is_perfect(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_perfect(root.left) and is_perfect(root.right) and \
               get_height(root.left) == get_height(root.right)
    return False

def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def determine_tree_type(root):
    num_nodes = count_nodes(root)
    if is_perfect(root):
        return "perfect"
    elif is_full(root):
        return "full"
    elif is_complete(root, 0, num_nodes):
        return "complete"
    else:
        return "neither complete nor full"

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

def load_blocks_from_csv(filename):
    blocks = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            block = {'id': row['id'], 'view': int(row['view']), 'votes': int(row['votes'])}
            blocks.append(block)
    return blocks

blocks = load_blocks("block.csv")
votes_received = load_votes("voute.csv")
chain = build_chain(blocks, votes_received)
save_results(blocks, chain, "block_results.csv")
print("Дані оброблено. Результати записані у block_results.csv.")

blocks = load_blocks_from_csv("block_results.csv")
bst_root = build_bst(blocks)
tree_type = determine_tree_type(bst_root)
print(f"Тип дерева: {tree_type}")
print("Pre-order обхід:")
preorder_traversal(bst_root)
print("\nIn-order обхід:")
inorder_traversal(bst_root)
print("\nPost-order обхід:")
postorder_traversal(bst_root)
print()