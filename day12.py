#!/usr/bin/python3

import sys

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
            if op == 'cpy':
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
 
        # Execute
        try:
            pc = 0
            while pc < len_code:
                inst = code[pc]

                op = inst[0]
                if op == 'cpy':
                    self.regs[ord(inst[2]) - 97] = self.immediate_or_value(inst[1])
                elif op == 'inc':
                    self.regs[ord(inst[1]) - 97] += 1
                elif op == 'dec':
                    self.regs[ord(inst[1]) - 97] -= 1
                elif op == 'jnz':
                    if self.immediate_or_value(inst[1]) != 0:
                        pc += inst[2]
                        continue

                pc += 1
        except Exception as e:
            print(f'Exception while executing instruction {inst}: "{e}"\n\nRegisters: {self.regs}')
            sys.exit(1)


with open(sys.argv[1]) as f:
    program = f.read()

cpu = CPU()
cpu.run(program)
print(f'Part 1: {cpu.a}')

cpu = CPU(c=1)
cpu.run(program)
print(f'Part 2: {cpu.a}')

