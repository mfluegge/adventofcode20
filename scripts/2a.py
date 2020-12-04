from pathlib import Path

with open(Path("../problems/2.txt"), "r") as f:
    data = [l.strip() for l in f.readlines()]

def count_occurences(s, char):
    return len([c for c in s if c==char])

valid = 0
for line in data:
    freq, char, pw = line.split(" ")
    char = char[:-1]
    freq_min, freq_max = freq.split("-")
    occ = count_occurences(pw, char)

    if int(freq_min) <= occ <= int(freq_max):
        valid += 1

print(valid)