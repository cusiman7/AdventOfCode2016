#!/usr/bin/python3

import sys
import copy

class CPU:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.regs = [a, b, c, d]

    @property
    def a(self):
        return self.regs[0]

    @property
    def b(self):
        return self.regs[1]

    @property
    def c(self):
        return self.regs[2]

    @property
    def d(self):
        return self.regs[3]

    def immediate_or_value(self, operand):
        if isinstance(operand, int):
            return operand
        else:
            return self.regs[ord(operand) - 97]

    def run(self, program):
        # Parse
        code = [line.split(' ') for line in program.split('\n')]
        len_code = len(code)

        for inst in code:
            op = inst[0]
            if op == 'cpy' or op == 'tgl':
                try:
                    inst[1] = int(inst[1])
                except:
                    pass
            elif op == 'jnz':
                try:
                    inst[1] = int(inst[1])
                except:
                    pass
                try:
                    inst[2] = int(inst[2])
                except:
                    pass
 
        counter = 0

        # Execute
        try:
            pc = 0
            while pc < len_code:
                inst = code[pc]

                if counter == 10000:
                    #print(f'Sample {inst} Regs: {self.regs}')
                    counter = 0

                op = inst[0]
                if op == 'cpy':
                    if isinstance(inst[2], str):
                        self.regs[ord(inst[2]) - 97] = self.immediate_or_value(inst[1])
                elif op == 'inc':
                    if isinstance(inst[1], str):
                        self.regs[ord(inst[1]) - 97] += 1
                elif op == 'dec':
                    if isinstance(inst[1], str):
                        self.regs[ord(inst[1]) - 97] -= 1
                elif op == 'mac':
                    a = self.immediate_or_value(inst[1])
                    b = self.immediate_or_value(inst[2])
                    print(f'mac {self.regs[ord(inst[3]) - 97]} += {a} * {b}', end=' -> ')
                    self.regs[ord(inst[3]) - 97] += a * b
                    print(f'Regs: {self.regs}')
                elif op == 'jnz':
                    if self.immediate_or_value(inst[1]) != 0:
                        pc += self.immediate_or_value(inst[2])
                        continue
                elif op == 'tgl':
                    x = pc + self.immediate_or_value(inst[1])

                    if x < 0 or x > len_code:
                        pass
                    elif len(code[x]) == 2:
                        code[x][0] = 'dec' if code[x][0] == 'inc' else 'inc'
                    elif len(code[x]) == 3:
                        code[x][0] = 'cpy' if code[x][0] == 'jnz' else 'jnz'

                    # Optimize
                    for i in range(len(code) - 6):
                        if code[i][0] == 'cpy' and \
                            code[i+1][0] == 'inc' and \
                            code[i+2][0] == 'dec' and \
                            code[i+3][0] == 'jnz' and code[i+3][2] == -2 and \
                            code[i+4][0] == 'dec' and \
                            code[i+5][0] == 'jnz' and code[i+5][2] == -5:

                            print('Multiply Acc Found:')
                            for j in range(i, i+5):
                                print(' '.join([str(op) for op in code[j]]))

                            code[i] = ['mac', code[i+4][1], code[i][1], code[i+1][1]]
                            code[i+1] = ['jnz', 0, 0]
                            code[i+2] = ['jnz', 0, 0]
                            code[i+3] = ['jnz', 0, 0]
                            code[i+4] = ['jnz', 0, 0]
                            code[i+5] = ['jnz', 0, 0]

                            print(f'Becomes:')
                            for j in range(i, i+5):
                                print(' '.join([str(op) for op in code[j]]))

                pc += 1
                counter += 1
        except Exception as e:
            print(f'Exception while executing instruction {inst}: "{e}"\n\nRegisters: {self.regs}')
            sys.exit(1)


with open(sys.argv[1]) as f:
    program = f.read()

cpu = CPU(a=7)
cpu.run(copy.copy(program))
print(f'Part 1: {cpu.a}')

cpu = CPU(a=12)
cpu.run(program)
print(f'Part 2: {cpu.a}')

