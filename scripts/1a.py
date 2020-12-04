from pathlib import Path

with open(Path("../problems/1.txt"), "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

sorted_data = sorted(data)
for big in sorted_data[::-1]:
    for small in sorted_data:
        s = big + small
        if s == 2020:
            print(big * small)
            exit()
        elif s > 2020:
            break
