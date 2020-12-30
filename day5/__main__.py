
from day5 import boardingpass

BOARDING_PASSES = open('day5/input.txt', 'r')
bp_array = BOARDING_PASSES.read().splitlines()

ids_found = set()
possible_ids = set()


for bp in bp_array:

    row_text = boardingpass.get_row_text(bp)
    col_text = boardingpass.get_col_text(bp)

    row_value = boardingpass.get_binary_value(row_text, 'B', 'F')
    col_value = boardingpass.get_binary_value(col_text, 'R', 'L')

    id = boardingpass.get_id(row_value, col_value)
    ids_found.add(id)

    if id in possible_ids:
        possible_ids.remove(id)

    if ((id-2) in ids_found) and (not ((id-1) in ids_found)):
        possible_ids.add(id-1)
    if((id+2) in ids_found) and (not ((id+1) in ids_found)):
        possible_ids.add(id+1)

print(possible_ids)
