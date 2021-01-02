
from day8 import handheld

INSTRUCTIONS = open('day8/input.txt', 'r')
instructions_array = INSTRUCTIONS.read().splitlines()


index, acc, visited = handheld.modify_loop(instructions_array)
print(acc)
