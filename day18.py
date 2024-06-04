#!/usr/bin/env python3

def trap_rule(row):
    if row == '^^.' or row == '.^^' or row == '^..' or row == '..^':
        return '^'
    return '.'

def total_safe(first_row, row_count):
    row_num = 0
    total = 0
    row = first_row
    while row_num < row_count:
        new_row = ''
        new_row += trap_rule('.' + row[:2])

        for i in range(1, len(row) - 1):
            new_row += trap_rule(row[i-1:i+2])

        new_row += trap_rule(row[-2:] + '.')

        total += row.count('.')
        row = new_row
        row_num += 1

    return total

row = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
print(f'Part 1: {total_safe(row, 40)}')
print(f'Part 2: {total_safe(row, 400000)}')
