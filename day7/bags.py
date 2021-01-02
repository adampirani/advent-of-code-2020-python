# This is scary inefficent.
# Space complexity is O(n) for uknown_bags (can take 3x space\) + bags_with_type + bags_without type
# Time complexity is
# Initial process bags:
#   O(n) (intial_process_bags)
# * Process_bag
#   [2*O(k) length of string + O(2) for inner bags]
# + reprocess_bags
# O(n^2) * (O(n^2 + n) = O(n^4)

import re


def process_bag(bag, bag_type, unknown_bags={}, bags_with_type=set(), bags_without_type=set()):

    bag_breakdown = bag.split(' bags contain ')
    bag_name = bag_breakdown[0]
    if bag_name == bag_type:
        return
    if bag.find('contain no other bags') > -1:
        bags_without_type.add(bag_name)
    else:
        bag_contents = bag_breakdown[1]
        # trim ' bag(s).'
        final_bag_idx = bag_contents.rfind(' bag')
        bag_contents = bag_contents[:final_bag_idx]
        inner_bags = re.split(' bags?, ', bag_contents)
        potential_uknown_bag = {}
        is_uknown = True
        for inner_bag in inner_bags:
            inner_bag_name = inner_bag[2:]
            inner_bag_amount = int(inner_bag[0])
            if inner_bag_name == bag_type:
                bags_with_type.add(bag_name)
                is_uknown = False
                break
            else:
                potential_uknown_bag[inner_bag_name] = inner_bag_amount
        if is_uknown:
            unknown_bags[bag_name] = potential_uknown_bag

    return unknown_bags, bags_with_type, bags_without_type


def intial_process_bags(array_of_bags, bag_type, num_bags=1):
    unknown_bags = {}
    bags_with_type = set()
    bags_without_type = set()

    for bag in array_of_bags:
        process_bag(bag, bag_type, unknown_bags,
                    bags_with_type, bags_without_type)

    return unknown_bags, bags_with_type, bags_without_type


def reprocess_bags(unknown_bags={}, bags_with_type=set(), bags_without_type=set()):
    newly_known_bags = set()
    while len(unknown_bags):  # Worst case O(n - 2) + O(n-3) + O(n-4)
        for bag_name, bag_contents in unknown_bags.items():  # Worst case O(n-2) + O(n-3) + O(n-4)
            still_unknown = False
            has_type = False
            for inner_bag in bag_contents:
                if (inner_bag in bags_with_type) or (inner_bag in bags_without_type):
                    if inner_bag in bags_with_type:
                        bags_with_type.add(bag_name)
                        still_unknown = False
                        has_type = True
                        break
                else:
                    still_unknown = True
            if not still_unknown:
                newly_known_bags.add(bag_name)
                if not has_type:
                    bags_without_type.add(bag_name)

        for newly_known_bag in newly_known_bags:  # Worst case 1 + 1 + 1
            del unknown_bags[newly_known_bag]
        newly_known_bags.clear()
