import unittest

from day1.src import products


class TestProduct(unittest.TestCase):

    def test_double(self):
        self.assertEqual(
            products.findProduct(
                2020, ["1721", "979", "366", "299", "675", "1456"]),
            514579
        )


if __name__ == '__main__':
    unittest.main()
