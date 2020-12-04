from pathlib import Path

with open(Path("../problems/2.txt"), "r") as f:
    data = [l.strip() for l in f.readlines()]

valid = 0
for line in data:
    pos, char, pw = line.split(" ")
    char = char[:-1]
    pos_1, pos_2 = pos.split("-")

    if (pw[int(pos_1) - 1] == char) ^ (pw[int(pos_2) - 1] == char):
        valid += 1

print(valid)