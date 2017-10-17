import sys


class BrainfuckInterpreter:
    def __init__(self, code, cells=10000, flush=True, file=sys.stdout):
        self.code = code
        self.pc = 0
        self.memory = [0] * cells
        self.pointer = 0
        self.flush = flush
        self.file = file

    def expr(self):
        current_instr = self.code[self.pc]
        if current_instr == '+':
            self.memory[self.pointer] += 1
        elif current_instr == '-':
            self.memory[self.pointer] -= 1
        elif current_instr == '>':
            self.pointer += 1
        elif current_instr == '<':
            self.pointer -= 1
        elif current_instr == '.':
            print(
                chr(self.memory[self.pointer]),
                flush=self.flush,
                end='',
                file=self.file,
            )
        elif current_instr == ',':
            self.memory[self.pointer] = sys.stdin.read(1)
        elif current_instr == '[' and self.memory[self.pointer] == 0:
            self.find_matching_square_bracket(']')
        elif current_instr == ']' and self.memory[self.pointer] != 0:
            self.find_matching_square_bracket('[')

    def find_matching_square_bracket(self, square_bracket):
        square_count = 1

        if square_bracket == '[':
            move_to = 1
        elif square_bracket == ']':
            move_to = -1

        while square_count > 0:
            self.pc -= move_to
            instr = self.code[self.pc]
            if instr == ']':
                square_count += move_to
            elif instr == '[':
                square_count -= move_to

    def eval(self):
        while self.pc < len(self.code):
            self.expr()
            self.pc += 1

    def run(self):
        self.eval()
