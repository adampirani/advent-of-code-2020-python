import unittest

from day5 import boardingpass


class TestBoardingPass(unittest.TestCase):

    def test_get_row_text(self):
        self.assertEqual(boardingpass.get_row_text('BFFFBBFRRR'), 'BFFFBBF')

    def test_get_col_text(self):
        self.assertEqual(boardingpass.get_col_text('BFFFBBFRRR'), 'RRR')

    def test_get_binary_value(self):
        self.assertEqual(
            boardingpass.get_binary_value('BFFFBBF', 'B', 'F'),
            70
        )
        self.assertEqual(
            boardingpass.get_binary_value('FFFBBBF', 'B', 'F'),
            14
        )
        self.assertEqual(
            boardingpass.get_binary_value('BBFFBBF', 'B', 'F'),
            102
        )
        self.assertEqual(
            boardingpass.get_binary_value('RRR', 'R', 'L'),
            7
        )
        self.assertEqual(
            boardingpass.get_binary_value('RLL', 'R', 'L'),
            4
        )

    def test_get_id(self):
        self.assertEqual(boardingpass.get_id(70, 7), 567)
        self.assertEqual(boardingpass.get_id(14, 7), 119)
        self.assertEqual(boardingpass.get_id(102, 4), 820)


if __name__ == '__main__':
    unittest.main()
