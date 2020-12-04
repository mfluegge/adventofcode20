from pathlib import Path
import time

with open(Path("../problems/1.txt"), "r") as f:
    data = [int(l.strip()) for l in f.readlines()]

sorted_data = sorted(data)
for big in sorted_data[::-1]:
    for small_ix, small in enumerate(sorted_data):
        sum1 = big + small
        if sum1 > 2020:
            break
        
        diff = 2020 - sum1

        if diff < small:
            break

        for mid in sorted_data[small_ix+1:]:
            sum2 = sum1 + mid
            
            if sum2 == 2020:
                print(big * mid * small)
                exit()

            if sum2 > 2020:
                break