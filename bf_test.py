from io import StringIO
import sys
import unittest

from bf import BrainfuckInterpreter


class BranfuckInterpreterTest(unittest.TestCase):
    def test_incr(self):
        bf = BrainfuckInterpreter('+')
        bf.run()
        self.assertEqual(bf.memory[0], 1)

    def test_decr(self):
        bf = BrainfuckInterpreter('-')
        bf.run()
        self.assertEqual(bf.memory[0], -1)

    def test_pointer_incr(self):
        bf = BrainfuckInterpreter('>')
        bf.run()
        self.assertEqual(bf.pointer, 1)

    def test_pointer_decr(self):
        bf = BrainfuckInterpreter('<')
        bf.run()
        self.assertEqual(bf.pointer, -1)

    def test_stdin_reading(self):
        old_stdin = sys.stdin
        sys.stdin = fake_stdin = StringIO('O')
        bf = BrainfuckInterpreter(',')
        bf.run()
        sys.stdin = old_stdin
        self.assertEqual(bf.memory[0], 'O')

    def test_hello_world(self):
        # from https://esolangs.org/wiki/Hello_world_program_in_esoteric_languages#Brainfuck  # noqa
        code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'  # noqa
        fake_stdout = StringIO()
        bf = BrainfuckInterpreter(code, file=fake_stdout)
        bf.run()
        self.assertEqual(fake_stdout.getvalue().strip(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
