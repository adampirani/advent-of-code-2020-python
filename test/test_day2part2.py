import unittest

from day2part2 import passwords


class TestPasswords(unittest.TestCase):

    def test_is_valid(self):
        self.assertEqual(
            passwords.is_valid('abcde', 'a', 1, 3),
            True
        )
        self.assertEqual(
            passwords.is_valid('cdefg', 'a', 1, 3),
            False
        )
        self.assertEqual(
            passwords.is_valid('ccccccccc', 'c', 2, 9),
            False
        )

    def test_split_line(self):
        split = passwords.split('1-3 a: abcde')
        self.assertEqual(split['min'], 1)
        self.assertEqual(split['max'], 3)
        self.assertEqual(split['letter'], 'a')
        self.assertEqual(split['password'], 'abcde')

    def test_split_line2(self):
        split = passwords.split('10-15 a: abcde')
        self.assertEqual(split['min'], 10)
        self.assertEqual(split['max'], 15)
        self.assertEqual(split['letter'], 'a')
        self.assertEqual(split['password'], 'abcde')

    def test_num_valid(self):
        sample = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"
        ]
        self.assertEqual(passwords.num_valid(sample), 1)


if __name__ == '__main__':
    unittest.main()
