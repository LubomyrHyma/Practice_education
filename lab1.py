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

blocks = load_blocks("block.csv")
votes_received = load_votes("voute.csv")
chain = build_chain(blocks, votes_received)
save_results(blocks, chain, "block_results.csv")

print("Дані оброблено. Результати записані у block_results.csv.")
