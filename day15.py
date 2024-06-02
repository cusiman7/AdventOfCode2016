#!/usr/bin/env python3

discs = [(5, 17), (8, 19), (1, 7), (7, 13), (1, 5), (0, 3)]
discs2 = [(5, 17), (8, 19), (1, 7), (7, 13), (1, 5), (0, 3), (0, 11)]

def calculate_timing(discs):
    t = 0
    while True:
        success = True 

        for i, disc in enumerate(discs):
            success = success and (disc[0] + i + t + 1) % disc[1] == 0
            
            if not success:
                break

        if success:
            return t

        t += 1

print(f'Part 1: {calculate_timing(discs)}')
print(f'Part 2: {calculate_timing(discs2)}')

