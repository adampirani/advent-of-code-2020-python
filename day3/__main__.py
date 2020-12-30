
from day3 import toboggan

MAP = open('day3/input.txt', 'r')
map_array = MAP.read().splitlines()

print(
    toboggan.num_trees(map_array, 0, 0, 1, 1) *
    toboggan.num_trees(map_array, 0, 0, 1, 3) *
    toboggan.num_trees(map_array, 0, 0, 1, 5) *
    toboggan.num_trees(map_array, 0, 0, 1, 7) *
    toboggan.num_trees(map_array, 0, 0, 2, 1)
)
