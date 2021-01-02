import unittest

from day6 import customs


class TestCustoms(unittest.TestCase):

    def test_num_yes(self):
        sample = [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b"
        ]
        self.assertEquals(customs.num_yes(sample), 6)


if __name__ == '__main__':
    unittest.main()
