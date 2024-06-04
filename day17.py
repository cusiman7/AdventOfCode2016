#!/usr/bin/env python3

import hashlib
from collections import deque

def md5(v):
    return hashlib.md5(v.encode()).hexdigest()

def shortest_path(passcode):
    dirs = [(0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R')]

    q = deque()
    q.append((0, 0, passcode))

    while q:
        x, y, path = q.popleft()

        if x == 3 and y == 3:
            return path[len(passcode):]

        key = md5(path)

        for i, (dx, dy, step) in enumerate(dirs):
            new_x = x + dx
            new_y = y + dy

            if new_x >= 0 and new_x <= 3 and new_y >= 0 and new_y <= 3 and key[i] in 'bcdef':
                q.append((new_x, new_y, path + step))

def longest_path_length(passcode):
    dirs = [(0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R')]

    visited = set()
    q = deque()

    visited.add((0, 0, passcode))
    q.append((0, 0, passcode))

    longest_path_length = 0

    while q:
        x, y, path = q.popleft()

        path_length = len(path[len(passcode):])
        if x == 3 and y == 3:
            if path_length > longest_path_length:
                longest_path_length = path_length 
            continue

        key = md5(path)

        for i, (dx, dy, step) in enumerate(dirs):
            new_x = x + dx
            new_y = y + dy
            n = (new_x, new_y, path + step)

            if new_x >= 0 and new_x <= 3 and new_y >= 0 and new_y <= 3 and n not in visited and key[i] in 'bcdef':
                visited.add(n)
                q.append(n)

    return longest_path_length

passcode = 'gdjjyniy'
print(f'Part 1: {shortest_path(passcode)}')
print(f'Part 2: {longest_path_length(passcode)}')

