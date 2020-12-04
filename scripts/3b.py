from pathlib import Path

with open(Path("../problems/3.txt"), "r") as f:
    data = [l.strip() for l in f.readlines()]

row_length = len(data[0])

def get_num_trees(right, down):
    current_index = 0
    current_line = 0
    num_trees = 0
    while (current_line + down) < len(data):
        current_line += down
        current_index = (current_index + right) % row_length
        is_tree = data[current_line][current_index] == "#"
        num_trees += is_tree
    
    return num_trees

inputs = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

mul = 1
for inp in inputs:
    mul *= get_num_trees(*inp)

print(mul)