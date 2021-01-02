
from day7 import bags

BAGS = open('day7/input.txt', 'r')
bags_array = BAGS.read().splitlines()

unknown_bags, bags_with_type, bags_without_type = bags.intial_process_bags(
    bags_array, 'shiny gold')

bags.reprocess_bags(unknown_bags, bags_with_type, bags_without_type)

print(len(bags_with_type))
