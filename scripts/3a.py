from pathlib import Path

with open(Path("../problems/3.txt"), "r") as f:
    data = [l.strip() for l in f.readlines()]

row_length = len(data[0])

current_index = 0
current_line = 0
num_trees = 0
for step in range(len(data) - 1):
    current_line += 1
    current_index = (current_index + 3) % row_length
    is_tree = data[current_line][current_index] == "#"
    num_trees += is_tree

print(num_trees)