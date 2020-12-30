import unittest

from day3 import toboggan


class TestPasswords(unittest.TestCase):

    def test_is_hit(self):
        self.assertFalse(toboggan.is_hit("..##......#", 0))
        self.assertFalse(toboggan.is_hit("..##......#", 1))
        self.assertTrue(toboggan.is_hit("..##......#", 2))
        self.assertTrue(toboggan.is_hit("..##......#", 10))
        self.assertFalse(toboggan.is_hit("..##......#", 11))
        self.assertFalse(toboggan.is_hit("..##......#", 12))
        self.assertTrue(toboggan.is_hit("..##......#", 13))

    def test_num_trees(self):
        sample = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]
        self.assertEqual(toboggan.num_trees(sample), 7)


if __name__ == '__main__':
    unittest.main()
