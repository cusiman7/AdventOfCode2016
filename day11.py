#!/usr/bin/python3

import sys
import itertools
import copy
from collections import deque


class State:
    def __init__(self, floors, elevator):
        self.floors = floors
        self.elevator = elevator

    def encode(self):
        state = ''
        for level, floor in enumerate(self.floors):
            state += str(level);
            
            if self.elevator == level:
                state += 'E'

            state += ''.join(sorted(floor))

        return state

    def is_done(self):
        return self.elevator == 3 and \
            len(self.floors[0]) == 0 and \
            len(self.floors[1]) == 0 and \
            len(self.floors[2]) == 0

    def is_valid(self):
        for floor in self.floors:
            rtg_elements = [rtg.split('_')[1] for rtg in filter(lambda x: x.startswith('G'), floor)]

            if len(rtg_elements) > 0:
                for chip in filter(lambda x: x.startswith('M'), floor):
                    chip_element = chip.split('_')[1]

                    if chip_element not in rtg_elements:
                        return False

        return True

    def generate_next_states(self):
        singles = [(x, None) for x in self.floors[self.elevator]]
        pairs = list(itertools.combinations(self.floors[self.elevator], 2))

        items = singles + pairs

        moves = []
        if self.elevator > 0:
            moves.extend([(x[0], x[1], self.elevator - 1) for x in items])

        if self.elevator < 3:
            moves.extend([(x[0], x[1], self.elevator + 1) for x in items])

        for item1, item2, next_elevator in moves:
            next_floors = copy.deepcopy(self.floors)

            next_floors[self.elevator].remove(item1)
            if item2:
                next_floors[self.elevator].remove(item2)

            next_floors[next_elevator].append(item1)
            if item2:
                next_floors[next_elevator].append(item2)

            next_state = State(next_floors, next_elevator)

            if next_state.is_valid():
                yield next_state

    def __str__(self):
        s = ''
        for i, floor in reversed(list(enumerate(self.floors))):
            s += f'F{i} '
            if self.elevator == i:
                s += 'E '
            s += ' ' .join(floor)
            s += '\n'
        return s


lines = []
with open(sys.argv[1]) as f:
    for line in f:
        tokens = line.rstrip().replace(',', '').replace('.', '').split(' ')
        lines.append(tokens)

floors = []
for line in lines:
    floor = []
    for token_index, token in enumerate(line):
        if token == 'generator':
            element = line[token_index - 1] 
            floor.append('G_' + element)

        if '-' in token:
            element = token.split('-')[0]
            floor.append('M_' + element)

    floors.append(floor)

first_state = State(floors, 0)
first_state.depth = 0

visited = set()
visited.add(first_state.encode())

q = deque()
q.appendleft(first_state)

while len(q) > 0:
    state = q.pop()
    #print(state)

    if state.is_done():
        print(f'Found {state.depth}')
        break

    depth = state.depth

    for next_state in state.generate_next_states():
        next_state.depth = depth + 1

        encoded_state = next_state.encode()
        if encoded_state not in visited:
            #print(encoded_state)
            visited.add(encoded_state)
            q.appendleft(next_state)

print(f'Done {len(visited)} states visited')
