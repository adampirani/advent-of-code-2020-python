import unittest

from day8 import handheld


class TestHandHeld(unittest.TestCase):

    def test_process_instruction_nop(self):

        index = 0
        acc = 0
        visited = set()

        index, acc, visited = handheld.process_instruction(
            "nop +0", index, acc, visited)

        self.assertEqual(index, 1)
        self.assertEqual(acc, 0)
        self.assertTrue(0 in visited)

    def test_process_instruction_acc(self):

        index = 0
        acc = 0
        visited = set()

        index, acc, visited = handheld.process_instruction(
            "acc +5", index, acc, visited)

        self.assertEqual(index, 1)
        self.assertEqual(acc, 5)
        self.assertTrue(0 in visited)

        index, acc, visited = handheld.process_instruction(
            "acc -4", index, acc, visited)

        self.assertEqual(index, 2)
        self.assertEqual(acc, 1)
        self.assertTrue(1 in visited)

    def test_process_instruction_jmp(self):

        index = 0
        acc = 0
        visited = set()

        index, acc, visited = handheld.process_instruction(
            "jmp +5", index, acc, visited)

        self.assertEqual(index, 5)
        self.assertEqual(acc, 0)
        self.assertTrue(0 in visited)

        index, acc, visited = handheld.process_instruction(
            "jmp -1", index, acc, visited)

        self.assertEqual(index, 4)
        self.assertEqual(acc, 0)
        self.assertTrue(0 in visited)

    def test_find_loop(self):
        sample = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
        index, acc, visited = handheld.find_loop(sample)

        self.assertEqual(index, 1)
        self.assertEqual(acc, 5)
        self.assertTrue(handheld.has_loop(index, len(sample)))

    def test_has_loop_false(self):

        sample = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "nop -4",
            "acc +6",
        ]
        index, acc, visited = handheld.find_loop(sample)

        self.assertEqual(acc, 8)
        self.assertFalse(handheld.has_loop(index, len(sample)))


if __name__ == '__main__':
    unittest.main()
