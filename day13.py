#!/usr/bin/env python3

from collections import deque

designers_fav_num = 1350
target_x = 31
target_y = 39

def is_open(x, y):
    value = x*x + 3*x + 2*x*y + y + y*y
    value += designers_fav_num 
    return bin(value).count("1") % 2 == 0

visited = set()
q = deque()

visited.add((1, 1))
q.append((1, 1, 0))

while q:
    x, y, depth = q.popleft()

    if x == target_x and y == target_y:
        print(f'At target {depth}')
        break

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in dirs:
        new_x = x + dx
        new_y = y + dy
        new_depth = depth + 1

        if new_x >= 0 and new_y >= 0 and (new_x, new_y) not in visited and is_open(new_x, new_y) and new_depth <= 50:
            visited.add((new_x, new_y))
            q.append((new_x, new_y, new_depth))

print(f'Done: {len(visited)}')
