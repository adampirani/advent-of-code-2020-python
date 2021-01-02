
from day6 import customs

CUSTOMS = open('day6/input.txt', 'r')
customs_array = CUSTOMS.read().splitlines()

print(customs.num_yes(customs_array))
