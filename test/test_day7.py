import unittest

from day7 import bags


class TestBags(unittest.TestCase):

    def test_process_bag_unknown(self):

        unknown_bags = {}
        bags_with_type = {}
        bags_without_type = {}

        bag = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        bags.process_bag(
            bag,
            'shiny gold',
            unknown_bags,
            bags_with_type,
            bags_without_type
        )

        self.assertEquals(
            unknown_bags['light red'],
            {'bright white': 1, 'muted yellow': 2}
        )

    def test_process_bag_known(self):

        unknown_bags = {}
        bags_with_type = set()
        bags_without_type = set()

        bags.process_bag(
            "bright white bags contain 1 shiny gold bag.",
            'shiny gold',
            unknown_bags,
            bags_with_type,
            bags_without_type
        )

        self.assertEquals(
            len(unknown_bags),
            0
        )
        self.assertTrue(
            'bright white' in bags_with_type
        )
        self.assertFalse(
            'bright white' in bags_without_type
        )

        bags.process_bag(
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            'shiny gold',
            unknown_bags,
            bags_with_type,
            bags_without_type
        )

        bags.reprocess_bags(unknown_bags, bags_with_type, bags_without_type)

        self.assertTrue(
            'light red' in bags_with_type
        )
        self.assertEquals(
            len(unknown_bags),
            0
        )

    def test_process_and_reprocess(self):

        sample = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]

        unknown_bags, bags_with_type, bags_without_type = bags.intial_process_bags(
            sample, 'shiny gold')

        bags.reprocess_bags(unknown_bags, bags_with_type, bags_without_type)

        self.assertEqual(len(bags_with_type), 4)


if __name__ == '__main__':
    unittest.main()
