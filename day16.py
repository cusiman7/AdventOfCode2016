#!/usr/bin/env python3

def fill_disk(state, size):
    while len(state) < size:
        b = state
        state += '0'

        for c in reversed(b):
            if c == '0':
                state += '1'
            else:
                state += '0'
    return state[:size]

def calculate_checksum(state):

    def checksum_internal(state):
        result = ''
        for a, b in zip(state[::2], state[1::2]):
            if a == b:
                result += '1'
            else:
                result += '0'
        return result

    checksum = checksum_internal(state)
    while len(checksum) % 2 == 0:
        checksum = checksum_internal(checksum)

    return checksum 

state = fill_disk('10111011111001111', 272)
checksum = calculate_checksum(state) 
print(f'Part 1: {checksum}')

state = fill_disk('10111011111001111', 35651584)
checksum = calculate_checksum(state) 
print(f'Part 2: {checksum}')

